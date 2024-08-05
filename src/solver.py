import numpy as np

def calculate_link_loads(geometry):
    loads = {
        'trackrod': {'Fx': 0, 'Fy': 0, 'Fz': 0, 'Mx': 0, 'My': 0, 'Mz': 0},
        'pushrod': {'Fx': 0, 'Fy': 0, 'Fz': 0, 'Mx': 0, 'My': 0, 'Mz': 0},
        'lower_fwd': {'Fx': 0, 'Fy': 0, 'Fz': 0, 'Mx': 0, 'My': 0, 'Mz': 0},
        'lower_rwd': {'Fx': 0, 'Fy': 0, 'Fz': 0, 'Mx': 0, 'My': 0, 'Mz': 0},
        'upper_fwd': {'Fx': 0, 'Fy': 0, 'Fz': 0, 'Mx': 0, 'My': 0, 'Mz': 0},
        'upper_rwd': {'Fx': 0, 'Fy': 0, 'Fz': 0, 'Mx': 0, 'My': 0, 'Mz': 0},
    }

    relative_positions_to_upright = {
        'trackrod': {'x': 0, 'y': 0, 'z': 0},
        'pushrod': {'x': 0, 'y': 0, 'z': 0},
        'lower_fwd': {'x': 0, 'y': 0, 'z': 0},
        'lower_rwd': {'x': 0, 'y': 0, 'z': 0},
        'upper_fwd': {'x': 0, 'y': 0, 'z': 0},
        'upper_rwd': {'x': 0, 'y': 0, 'z': 0},
    }

    relative_positions_to_contact_patch = {
        'trackrod': {'x': 0, 'y': 0, 'z': 0},
        'pushrod': {'x': 0, 'y': 0, 'z': 0},
        'lower_fwd': {'x': 0, 'y': 0, 'z': 0},
        'lower_rwd': {'x': 0, 'y': 0, 'z': 0},
        'upper_fwd': {'x': 0, 'y': 0, 'z': 0},
        'upper_rwd': {'x': 0, 'y': 0, 'z': 0},
    }

    unit_vectors = {
        'trackrod': {'x': 0, 'y': 0, 'z': 0},
        'pushrod': {'x': 0, 'y': 0, 'z': 0},
        'lower_fwd': {'x': 0, 'y': 0, 'z': 0},
        'lower_rwd': {'x': 0, 'y': 0, 'z': 0},
        'upper_fwd': {'x': 0, 'y': 0, 'z': 0},
        'upper_rwd': {'x': 0, 'y': 0, 'z': 0},
    }

    cross_products = {
        'trackrod': {'x': 0, 'y': 0, 'z': 0},
        'pushrod': {'x': 0, 'y': 0, 'z': 0},
        'lower_fwd': {'x': 0, 'y': 0, 'z': 0},
        'lower_rwd': {'x': 0, 'y': 0, 'z': 0},
        'upper_fwd': {'x': 0, 'y': 0, 'z': 0},
        'upper_rwd': {'x': 0, 'y': 0, 'z': 0},
    }

    # relative_positions_to_upright calculation
    # Iterate over each link type in loads
    for link_type in loads: 
        # Get the hardpoint name based on link_type
        if link_type == 'trackrod':
            link_hp = geometry.hardpoint_dict.get('trackrod chassis')
            upright_hp = geometry.hardpoint_dict.get('trackrod upright')
        elif link_type == 'pushrod':
            link_hp = geometry.hardpoint_dict.get('pushrod chassis')
            upright_hp = geometry.hardpoint_dict.get('pushrod upright')
        elif link_type == 'lower_fwd':
            link_hp = geometry.hardpoint_dict.get('lower fwd')
            upright_hp = geometry.hardpoint_dict.get('lower upright')
        elif link_type == 'lower_rwd':
            link_hp = geometry.hardpoint_dict.get('lower rwd')
            upright_hp = geometry.hardpoint_dict.get('lower upright')
        elif link_type == 'upper_fwd':
            link_hp = geometry.hardpoint_dict.get('upper fwd')
            upright_hp = geometry.hardpoint_dict.get('upper upright')
        elif link_type == 'upper_rwd':
            link_hp = geometry.hardpoint_dict.get('upper rwd')
            upright_hp = geometry.hardpoint_dict.get('upper upright')

        # Calculate the relative positions
        rel_x = link_hp.x - upright_hp.x
        rel_y = link_hp.y - upright_hp.y
        rel_z = link_hp.z - upright_hp.z

        # Populate the relative_positions dictionary with the calculated values
        relative_positions_to_upright[link_type]['x'] = rel_x
        relative_positions_to_upright[link_type]['y'] = rel_y
        relative_positions_to_upright[link_type]['z'] = rel_z
    
    # Print the relative positions for verification. Works I think
    # for link_type, position in relative_positions_to_upright.items():
    #     print(f"{link_type}: x = {position['x']}, y = {position['y']}, z = {position['z']}")

    # relative_positions_to_contact_patch calculation
    # Iterate over each link type in loads
    for link_type in loads: 
        # Get the hardpoint name based on link_type
        if link_type == 'trackrod':
            link_hp = geometry.hardpoint_dict.get('trackrod upright')
        elif link_type == 'pushrod':
            link_hp = geometry.hardpoint_dict.get('pushrod upright')
        elif link_type == 'lower_fwd':
            link_hp = geometry.hardpoint_dict.get('lower upright')
        elif link_type == 'lower_rwd':
            link_hp = geometry.hardpoint_dict.get('lower upright')
        elif link_type == 'upper_fwd':
            link_hp = geometry.hardpoint_dict.get('upper upright')
        elif link_type == 'upper_rwd':
            link_hp = geometry.hardpoint_dict.get('upper upright')

        contact_patch_hp = geometry.hardpoint_dict.get('contact patch')

        # Calculate the relative positions
        rel_x = (link_hp.x - contact_patch_hp.x)/1000
        rel_y = (link_hp.y - contact_patch_hp.y)/1000
        rel_z = (link_hp.z - contact_patch_hp.z)/1000

        # Populate the relative_positions dictionary with the calculated values
        relative_positions_to_contact_patch[link_type]['x'] = rel_x
        relative_positions_to_contact_patch[link_type]['y'] = rel_y
        relative_positions_to_contact_patch[link_type]['z'] = rel_z
    
    # Print the relative positions for verification. Works I think
    # for link_type, position in relative_positions_to_contact_patch.items():
    #     print(f"{link_type}: x = {position['x']}, y = {position['y']}, z = {position['z']}")

    # Unit vector calculation
    # Iterate over each link type in loads
    for link_type in loads: 
        link_hp = relative_positions_to_upright[link_type]

        norm = np.sqrt(
            link_hp['x']**2 +
            link_hp['y']**2 +
            link_hp['z']**2
        )

        unit_vectors[link_type]['x'] = link_hp['x'] / norm
        unit_vectors[link_type]['y'] = link_hp['y'] / norm
        unit_vectors[link_type]['z'] = link_hp['z'] / norm
    
    # Print the relative positions for verification. Works I think
    # for link_type, position in unit_vectors.items():
    #     print(f"{link_type}: x = {unit_vectors[link_type]['x']}, y = {unit_vectors[link_type]['y']}, z = {unit_vectors[link_type]['z']}")

        # cross_products calculation
    # Iterate over each link type in loads
    for link_type in loads: 
        # Calculate the relative positions
        rel_x = (relative_positions_to_contact_patch[link_type]['y']) * (unit_vectors[link_type]['z']) - (relative_positions_to_contact_patch[link_type]['z']) * (unit_vectors[link_type]['y'])
        rel_y = (relative_positions_to_contact_patch[link_type]['z']) * (unit_vectors[link_type]['x']) - (relative_positions_to_contact_patch[link_type]['x']) * (unit_vectors[link_type]['z'])
        rel_z = (relative_positions_to_contact_patch[link_type]['x']) * (unit_vectors[link_type]['y']) - (relative_positions_to_contact_patch[link_type]['y']) * (unit_vectors[link_type]['x'])

        # Populate the cross_products dictionary with the calculated values
        cross_products[link_type]['x'] = rel_x
        cross_products[link_type]['y'] = rel_y
        cross_products[link_type]['z'] = rel_z
    
    # Print the relative positions for verification. Works I think
    # for link_type, position in cross_products.items():
    #     print(f"{link_type}: x = {position['x']}, y = {position['y']}, z = {position['z']}")

    # Create the 6x6 matrix
    matrix = np.array([
        [unit_vectors['trackrod']['x'], unit_vectors['trackrod']['y'], unit_vectors['trackrod']['z'], cross_products['trackrod']['x'], cross_products['trackrod']['y'], cross_products['trackrod']['z']],
        [unit_vectors['pushrod']['x'], unit_vectors['pushrod']['y'], unit_vectors['pushrod']['z'], cross_products['pushrod']['x'], cross_products['pushrod']['y'], cross_products['pushrod']['z']],
        [unit_vectors['lower_fwd']['x'], unit_vectors['lower_fwd']['y'], unit_vectors['lower_fwd']['z'], cross_products['lower_fwd']['x'], cross_products['lower_fwd']['y'], cross_products['lower_fwd']['z']],
        [unit_vectors['lower_rwd']['x'], unit_vectors['lower_rwd']['y'], unit_vectors['lower_rwd']['z'], cross_products['lower_rwd']['x'], cross_products['lower_rwd']['y'], cross_products['lower_rwd']['z']],
        [unit_vectors['upper_fwd']['x'], unit_vectors['upper_fwd']['y'], unit_vectors['upper_fwd']['z'], cross_products['upper_fwd']['x'], cross_products['upper_fwd']['y'], cross_products['upper_fwd']['z']],
        [unit_vectors['upper_rwd']['x'], unit_vectors['upper_rwd']['y'], unit_vectors['upper_rwd']['z'], cross_products['upper_rwd']['x'], cross_products['upper_rwd']['y'], cross_products['upper_rwd']['z']],
    ])

    # Compute the inverse of the matrix
    matrix_inv = np.linalg.inv(matrix)

    # Define basis vectors
    basis_vectors = {
    'fx': np.array([1, 0, 0, 0, 0, 0]),
    'fy': np.array([0, 1, 0, 0, 0, 0]),
    'fz': np.array([0, 0, 1, 0, 0, 0]),
    'mx': np.array([0, 0, 0, 1, 0, 0]),
    'my': np.array([0, 0, 0, 0, 1, 0]),
    'mz': np.array([0, 0, 0, 0, 0, 1])
    }

    # Compute the resulting columns
    results = {}
    for key, basis_vector in basis_vectors.items():
        results[key] = np.dot(matrix_inv.T, basis_vector)

    # Convert results to a matrix where rows are basis vectors and columns are force/torque components
    result_matrix = np.column_stack([results['fx'], results['fy'], results['fz'], results['mx'], results['my'], results['mz']])

    # print("Final 6x6 Result Matrix:")   
    # print(result_matrix)

    # Update the loads dictionary with the computed loads
    for i, link_type in enumerate(loads.keys()):
        loads[link_type]['Fx'] = float(result_matrix[i, 0])
        loads[link_type]['Fy'] = float(result_matrix[i, 1])
        loads[link_type]['Fz'] = float(result_matrix[i, 2])
        loads[link_type]['Mx'] = float(result_matrix[i, 3])
        loads[link_type]['My'] = float(result_matrix[i, 4])
        loads[link_type]['Mz'] = float(result_matrix[i, 5])

    # # Example: assign dummy data for demo
    # for i, name in enumerate(loads.keys()):
    #     loads[name] = {'Fx': i, 'Fy': i, 'Fz': i, 'Mx': i, 'My': i, 'Mz': i}
    
    return loads
