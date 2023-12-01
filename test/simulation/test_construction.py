import subprocess
import sys
import pathlib
import pytest
import festim as F

# ... (existing code for test_demos and test_demos_mpi)

def run_simulation_test(simulation, combination_type, valid_types, error_message):
    for combination in valid_types:
        setattr(simulation, combination_type, combination)

    invalid_types = ["coucou", True]

    for combination in invalid_types:
        with pytest.raises(TypeError, match=error_message):
            setattr(simulation, combination_type, combination)

def test_setting_traps():
    my_sim = F.Simulation()
    my_mat = F.Material(1, 1, 0)
    trap1 = F.Trap(1, 1, 1, 1, [my_mat], density=1)
    trap2 = F.Trap(2, 2, 2, 2, [my_mat], density=1)

    valid_types = [trap1, [trap1], [trap1, trap2], F.Traps([trap1, trap2])]
    error_message = "Accepted types for traps are list, festim.Traps or festim.Trap"

    run_simulation_test(my_sim, "traps", valid_types, error_message)

# Similarly, create functions for other test cases (test_setting_traps_wrong_type, test_setting_materials, etc.)
