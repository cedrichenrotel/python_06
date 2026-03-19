#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_import_transmutation.py                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 07:26:40 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/19 17:00:37 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_earth
from alchemy.potions import strength_potion


def main() -> None:
    print("=== Import Transmutation Mastery ===")
    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

    print("\nMethod 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal()}")

    print("\nMethod 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}\ncreate_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")
    print("\nAll import transmutation methods mastered")


if __name__ == "__main__":
    main()
