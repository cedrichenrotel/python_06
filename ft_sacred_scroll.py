#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_sacred_scroll.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 07:21:44 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/19 07:21:49 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def main() -> None:
    print("=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")

    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    for i in ["create_fire", "create_water", "create_earth", "create_air"]:
        try:
            print(f"alchemy.{i}(): {getattr(alchemy, i)()}")
        except AttributeError:
            print(f"alchemy.{i}: AttributeError - not exposed")

    print("\nPackage metadata")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
