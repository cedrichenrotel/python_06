#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  validator.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 13:05:37 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/19 14:01:31 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def validate_ingredients(ingredients: str) -> str:
    for i in ["air", "earth", "water", "fire"]:
        if i in ingredients:
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
