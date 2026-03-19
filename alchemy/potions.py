#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 10:30:41 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/19 17:34:03 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import (
    create_fire,
    create_water,
    create_earth,
    create_air
)


def healing_potion() -> str:
    return (f"Healing potion brewed with {create_fire()} "
            f"and {create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with {create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {create_air} and "
            f"{create_water}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed with all elements: {create_fire}, "
            f"{create_water}, {create_earth}, {create_air}")
