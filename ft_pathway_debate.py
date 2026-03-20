#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 10:00:16 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/20 07:51:03 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.transmutation
from alchemy.transmutation import lead_to_gold, stone_to_gem


def main() -> None:
    print("=== Pathway Debate Mastery ===")
    print("Testing Absolute Imports (basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")
    print(f"elixir_of_life(): {alchemy.transmutation.elixir_of_life()}")

    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
