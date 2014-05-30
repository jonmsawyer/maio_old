#####################################
# Minimum width and height settings #
#####################################
#
# When used together, Maio will not save a database entry for a given picture
# if the picture's dimensions (width x height) do not meet the minimum
# requirements. When MIN_INCLUSIVE is set to 'AND', then Maio will strictly
# check to see if the image meets both MIN_WIDTH and MIN_HEIGHT settings.
# When MIN_INCLUSIVE is set to 'OR', then Maio will check to see if the image
# meets either MIN_WIDTH or MIN_HEIGHT settings.

# MIN_WIDTH
# The number of minimum pixels wide to be considered a picture for Maio to get.
# Set MIN_WIDTH to None for infinite width.
# Example:
# MIN_WIDTH = None  # Inf
# MIN_WIDTH = 200  # 200 pixels wide
MIN_WIDTH = 200

# MIN_HEIGHT
# The number of minimum pixels high to be considered a picture for Maio to get.
# Set MIN_HEIGHT to None for infinite height.
# Example:
# MIN_HEIGHT = None  # Inf
# MIN_HEIGHT = 250  # 250 pixels wide
MIN_HEIGHT = 200

# MIN_INCLUSIVE
# Set to 'OR' if you wish Maio to check for either a minimum width or a minimum
# height. Set to 'AND' if you wish Maio to check for strictly minimum width and
# minimum height.
MIN_INCLUSIVE = 'OR'

