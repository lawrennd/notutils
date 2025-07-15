# Copyright 2014 Open Data Science Initiative and other authors. See AUTHORS.txt
# Licensed under the BSD 3-clause license (see LICENSE.txt)

import os
from typing import Optional, Union, Callable, Dict, Any, Tuple
import IPython

if int(IPython.__version__[0]) > 3:
    from ipywidgets import interact, fixed
else:
    from IPython.html.widgets.interaction import interact, fixed
from IPython.display import display, HTML, IFrame, Image, SVG


def display_url(target: str) -> None:
    """Display a URL in a Jupyter notebook to allow the user to click and check on information.
    
    With thanks to Fernando Perez for putting together the implementation!
    
    :param target: The URL to display
    :type target: str
    """
    prefix = u"http://" if not target.startswith("http") else u""
    target = prefix + target
    display(HTML(u'<a href="{t}" target=_blank>{t}</a>'.format(t=target)))


def iframe_url(
    target: str, 
    width: int = 500, 
    height: int = 400, 
    scrolling: bool = True, 
    border: int = 0, 
    frameborder: int = 0
) -> str:
    """Produce an iframe for displaying an item in HTML window.
    
    :param target: The target URL
    :type target: str
    :param width: The width of the iframe (default 500)
    :type width: int
    :param height: The height of the iframe (default 400)
    :type height: int
    :param scrolling: Whether or not to allow scrolling (default True)
    :type scrolling: bool
    :param border: Width of the border
    :type border: int
    :param frameborder: Width of the frameborder
    :type frameborder: int
    :return: HTML iframe string
    :rtype: str
    """
    prefix = u"http://" if not target.startswith("http") else u""
    target = prefix + target
    if scrolling:
        scroll_val = "yes"
    else:
        scroll_val = "no"
    return u'<iframe frameborder="{frameborder}" scrolling="{scrolling}" style="border:{border}px" src="{url}", width={width} height={height}></iframe>'.format(
        frameborder=frameborder,
        scrolling=scroll_val,
        border=border,
        url=target,
        width=width,
        height=height,
    )


def display_iframe_url(target: str, **kwargs: Any) -> None:
    """Display the contents of a URL in an IPython notebook.
    
    :param target: The target URL
    :type target: str

    .. seealso:: :func:`iframe_url` for additional arguments.
    """
    txt = iframe_url(target, **kwargs)
    display(HTML(txt))


def display_google_book(
    id: str, 
    page: Optional[Union[str, int]] = None, 
    width: int = 600, 
    height: int = 450, 
    **kwargs: Any
) -> None:
    """Display an embedded version of a Google book.
    
    :param id: The ID of the Google book to display
    :type id: str
    :param page: The start page for the book
    :type page: str or int, optional
    :param width: The width of the embedded book (default 600)
    :type width: int
    :param height: The height of the embedded book (default 450)
    :type height: int
    """
    if isinstance(page, int):
        url = "https://books.google.co.uk/books?id={id}&pg=PA{page}&output=embed".format(
            id=id, page=page
        )
    else:
        url = "https://books.google.co.uk/books?id={id}&pg={page}&output=embed".format(
            id=id, page=page
        )
    IFrame(url, width=width, height=height, **kwargs)


def code_toggle(start_show: bool = False, message: Optional[str] = None) -> None:
    """Toggle code visibility on and off in a notebook.
    
    The tip that this idea is based on is from Damian Kao (http://blog.nextgenetics.net/?e=102).
    
    :param start_show: Whether to display the code or not on first load (default False)
    :type start_show: bool
    :param message: The message used to toggle display of the code
    :type message: str, optional
    """
    html = "<script>\n"
    if message is None:
        message = (
            u"The raw code for this jupyter notebook can be hidden for easier reading."
        )
    if start_show:
        html += u"code_show=true;\n"
    else:
        html += u"code_show=false;\n"
    html += """function code_toggle() {
 if (code_show){
 $('div.input').show();
 } else {
 $('div.input').hide();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
"""
    html += (
        message
        + ' To toggle on/off the raw code, click <a href="javascript:code_toggle()">here</a>.'
    )
    display(HTML(html))


def display_prediction(
    basis: Union[Callable, Dict[str, Callable]],
    num_basis: int = 4,
    wlim: Tuple[float, float] = (-1.0, 1.0),
    fig: Optional[Any] = None,
    ax: Optional[Any] = None,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    num_points: int = 1000,
    offset: float = 0.0,
    **kwargs: Any
) -> None:
    """Interactive widget for displaying a prediction function based on summing separate basis functions.
    
    :param basis: A function handle that calls the basis functions
    :type basis: callable or dict
    :param num_basis: Number of basis functions to use (default 4)
    :type num_basis: int
    :param wlim: Limits for the basis function weights (default (-1.0, 1.0))
    :type wlim: tuple of float
    :param fig: Matplotlib figure object (optional)
    :type fig: matplotlib.figure.Figure, optional
    :param ax: Matplotlib axes object (optional)
    :type ax: matplotlib.axes.Axes, optional
    :param xlim: Limits of the x axis to use (optional)
    :type xlim: tuple of float, optional
    :param ylim: Limits of the y axis to use (optional)
    :type ylim: tuple of float, optional
    :param num_points: Number of points to plot (default 1000)
    :type num_points: int
    :param offset: Offset for the first basis function (default 0.0)
    :type offset: float
    """
    import numpy as np
    import pylab as plt

    if fig is not None:
        if ax is None:
            ax = fig.gca()

    if xlim is None:
        if ax is not None:
            xlim = ax.get_xlim()
        else:
            xlim = (-2.0, 2.0)
    if ylim is None:
        if ax is not None:
            ylim = ax.get_ylim()
        else:
            ylim = (-1.0, 1.0)

    # initialise X and set up W arguments.
    x = np.zeros((num_points, 1))
    x[:, 0] = np.linspace(xlim[0], xlim[1], num_points)
    param_args = {}
    for i in range(num_basis):
        lim = list(wlim)
        if i == 0:
            lim[0] += offset
            lim[1] += offset
        param_args["w_" + str(i)] = tuple(lim)

    # helper function for making basis prediction.
    def predict_basis(w, basis, x, num_basis, **kwargs):
        Phi = basis(x, num_basis, **kwargs)
        f = np.dot(Phi, w)
        return f, Phi

    if isinstance(basis, dict):
        use_basis = basis[list(basis.keys())[0]]
    else:
        use_basis = basis
    f, Phi = predict_basis(np.zeros((num_basis, 1)), use_basis, x, num_basis, **kwargs)
    if fig is None:
        fig, ax = plt.subplots(figsize=(12, 4))
        if ax is not None:
            ax.set_ylim(ylim)
            ax.set_xlim(xlim)

    if ax is not None:
        predline = ax.plot(x, f, linewidth=2)[0]
        basislines = []
        for i in range(num_basis):
            basislines.append(ax.plot(x, Phi[:, i], "r")[0])

        ax.set_ylim(ylim)
        ax.set_xlim(xlim)

        def generate_function(
            basis,
            num_basis,
            predline,
            basislines,
            basis_args,
            display_basis,
            offset,
            **kwargs
        ):
            w = np.zeros((num_basis, 1))
            for i in range(num_basis):
                w[i] = kwargs["w_" + str(i)]
            f, Phi = predict_basis(w, basis, x, num_basis, **basis_args)
            predline.set_xdata(x[:, 0])
            predline.set_ydata(f)
            for i in range(num_basis):
                basislines[i].set_xdata(x[:, 0])
                basislines[i].set_ydata(Phi[:, i])

            if display_basis:
                for i in range(num_basis):
                    basislines[i].set_alpha(1)  # make visible
            else:
                for i in range(num_basis):
                    basislines[i].set_alpha(0)
            display(fig)

        if not isinstance(basis, dict):
            basis = fixed(basis)

        plt.close(fig)
        interact(
            generate_function,
            basis=basis,
            num_basis=fixed(num_basis),
            predline=fixed(predline),
            basislines=fixed(basislines),
            basis_args=fixed(kwargs),
            offset=fixed(offset),
            display_basis=False,
            **param_args
        )


def display_plots(
    filebase: str, 
    directory: Optional[str] = None, 
    width: int = 600, 
    height: int = 450, 
    **kwargs: Any
) -> None:
    """Display a series of plots controlled by sliders.
    
    The function relies on Python string format functionality to index through a series of plots.
    
    :param filebase: Base filename with format placeholders for indexing
    :type filebase: str
    :param directory: Directory containing the plot files (optional)
    :type directory: str, optional
    :param width: Width of the displayed plots (default 600)
    :type width: int
    :param height: Height of the displayed plots (default 450)
    :type height: int
    """

    def show_figure(filebase: str, directory: Optional[str], width: int = 600, height: int = 450, **kwargs: Any) -> None:
        """Helper function to load in the relevant plot for display.
        
        :param filebase: Base filename with format placeholders
        :type filebase: str
        :param directory: Directory containing the plot files
        :type directory: str, optional
        :param width: Width of the displayed plot
        :type width: int
        :param height: Height of the displayed plot
        :type height: int
        :param **kwargs: Format arguments for the filename
        """
        _, ext = os.path.splitext(filebase)
        filename = filebase.format(**kwargs)
        if directory is not None:
            filename = directory + "/" + filename
        if ext.lower() == ".svg":
            display(SVG(data="{filename}".format(filename=filename)))
        elif ext.lower() in [".png", ".jpg", ".gif", ".jpeg"]:
            display(
                Image(
                    data="{filename}".format(filename=filename),
                    width=width,
                    height=height,
                )
            )
        elif ext.lower() in [".html"]:
            display(
                IFrame(
                    src="{filename}".format(filename=filename),
                    width=width,
                    height=height,
                )
            )

    interact(
        show_figure,
        filebase=fixed(filebase),
        directory=fixed(directory),
        width=fixed(width),
        height=fixed(height),
        **kwargs
    )
