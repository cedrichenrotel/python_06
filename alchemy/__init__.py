#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 10:32:08 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/18 18:30:34 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .elements import create_fire, create_water

__all__ = [create_fire, create_water]
