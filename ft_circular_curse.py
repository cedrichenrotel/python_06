#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 13:03:34 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/19 15:01:35 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.grimoire import record_spell, validate_ingredients


def main() -> None:
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    print(f'validate_ingredients("fire air"): '
          f'{validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): '
          f'{validate_ingredients("dragon scales")}')

    print("\nTesting spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", validate_ingredients("fire air"))}')
    print(f'record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", validate_ingredients("shadow"))}')


if __name__ == "__main__":
    main()



