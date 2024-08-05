from geometry import Geometry, Hardpoint
from inout import read_input, write_output
from solver import calculate_link_loads
from ursina_test import visualize_hardpoints

def main():
    input_data = read_input('data/input/example_input.json')
    # hardpoints = [Hardpoint(**hp) for hp in input_data['hardpoints']]
    hardpoints = [Hardpoint(name=hp['name'], x=hp['x'], y=hp['y'], z=hp['z']) for hp in input_data['hardpoints']]
    geometry = Geometry(hardpoints)
    loads = calculate_link_loads(geometry)
    print("Calculated Loads:\n", loads)
    write_output('data/output/example_output.json', loads)

    # Visualize hardpoints
    visualize_hardpoints(hardpoints, geometry)


if __name__ == "__main__":
    main()