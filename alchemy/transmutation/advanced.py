#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  advanced.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 10:03:15 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/19 11:10:05 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    return (f"Philosopher's stone created using {lead_to_gold()}"
            f"and {healing_potion()}")


def elixir_of_life() -> str:
    return ("Elixir of life: eternal youth achieved!")
