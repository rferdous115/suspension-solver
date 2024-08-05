from ursina import *
# from geometry import Geometry, Hardpoint

def create_cylinder(start, end, color):
    mid_point = (start + end) / 2
    height = distance(start, end)
    direction = (end - start).normalized()
    
    cylinder = Entity(model=Cylinder(height=height, radius=0.15, direction=direction), color=color)
    cylinder.position = mid_point
    cylinder.look_at(start)
    return cylinder

def visualize_hardpoints(hardpoints, geometry):
    # Initialize the Ursina app
    app = Ursina()

    # Create spheres for each hardpoint with a larger scale
    for hp in hardpoints:
        print(f"Creating sphere for hardpoint: {hp.name} at position ({hp.x}, {hp.y}, {hp.z})")
        # Scale down the hardpoint position
        scaled_position = (hp.x / 100, hp   .y / 100, hp.z / 100)
        sphere = Entity(model='sphere', color=color.red, scale=0.5, position=scaled_position)
        # Position the text relative to the scaled position
        Text(text=hp.name, position=(scaled_position[0], scaled_position[1] + 0.6, scaled_position[2]), scale=2)

    # Create infinite axes with ticks at 10 mm intervals, scaled down accordingly
    tick_interval = 10 / 100  # Scale interval to match hardpoint scaling
    axis_length = 1000 / 100  # Scale axis length to match hardpoint scaling

    # Ensure tick_interval is non-zero and a small integer
    tick_interval = max(1, int(tick_interval))

    # Create ticks along the x-axis
    for i in range(-int(axis_length), int(axis_length) + tick_interval, tick_interval):
        Entity(model='cube', color=color.red, scale=(0.2, 0.2, 0.2), position=(i, 0, 0))

    # Create ticks along the y-axis
    for i in range(-int(axis_length), int(axis_length) + tick_interval, tick_interval):
        Entity(model='cube', color=color.green, scale=(0.2, 0.2, 0.2), position=(0, i, 0))

    # Create ticks along the z-axis
    for i in range(-int(axis_length), int(axis_length) + tick_interval, tick_interval):
        Entity(model='cube', color=color.blue, scale=(0.2, 0.2, 0.2), position=(0, 0, i))

    # Create the lines for the axes
    Entity(model=Mesh(vertices=[Vec3(-axis_length, 0, 0), Vec3(axis_length, 0, 0)], mode='line', thickness=2), color=color.red)
    Entity(model=Mesh(vertices=[Vec3(0, -axis_length, 0), Vec3(0, axis_length, 0)], mode='line', thickness=2), color=color.green)
    Entity(model=Mesh(vertices=[Vec3(0, 0, -axis_length), Vec3(0, 0, axis_length)], mode='line', thickness=2), color=color.blue)

    # Define linkages
    linkages = [
        ('trackrod chassis', 'trackrod upright', color.gray),
        ('pushrod chassis', 'pushrod upright', color.green),
        ('lower fwd', 'lower upright', color.yellow),
        ('lower rwd', 'lower upright', color.yellow),
        ('upper fwd', 'upper upright', color.yellow),
        ('upper rwd', 'upper upright', color.yellow)
    ]

    # Create cylinders for each linkage
    for hp in hardpoints:
        if hp.name == 'trackrod chassis':
            rel_hp = geometry.hardpoint_dict['trackrod upright']
            print(f"Start: ({hp.x / 100}, {hp.y / 100}, {hp.z / 100}), End: ({rel_hp.x / 100}, {rel_hp.y / 100}, {rel_hp.z / 100})")
            create_cylinder(Vec3(hp.x / 100, hp.y / 100, hp.z / 100), Vec3(rel_hp.x / 100, rel_hp.y / 100, rel_hp.z / 100), color.green)
            # print(f"Creating cylinder: start={start}, end={end}, direction={direction}")

    # Create spheres for each hardpoint for better visualization
    for hp in hardpoints:
        sphere = Entity(model='sphere', color=color.white, scale=0.1, position=Vec3(hp.x, hp.y, hp.z))

    # Create text to display camera coordinates
    coordinates_text = Text(
        text=f'Camera Position: {camera.position}',
        position=(0.5, -0.5),
        origin=(0.5, 0.5),
        scale=2,
        color=color.white
    )

    # Update the text with the camera's current position every frame
    def update():
        coordinates_text.text = f'Camera Position: {camera.position}'

    # Bind the update function to every frame
    camera.on_update = update

    # Set up the environment
    EditorCamera()

    # Run the app
    app.run()