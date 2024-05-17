'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    return ('<span style="font-family: Roboto Slabk"><b>Neighborhood : </b></span>%{y}'
            +'<br><span style="font-family: Roboto Slabk"><b>Year : </b></span>%{x}</br>'
            +'<span style="font-family: Roboto Slabk"><b>Trees planted : </b></span>%{z}<extra></extra>')

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template

