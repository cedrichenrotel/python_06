#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 10:30:41 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/19 13:04:56 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_fire, create_water, create_earth


def healing_potion() -> str:
    return (f"Healing potion brewed with {create_fire()} element created "
            f"and {create_water()} element created")


def strength_potion() -> str:
    return (f"Strength potion brewed with {create_earth()} element created "
            f"and {create_fire()} element created")
