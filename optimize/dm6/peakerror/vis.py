from vispy import scene

#canvas = scene.SceneCanvas(keys='interactive', show=False, size=(100,100))
#view = canvas.central_widget.add_view()
#view.parent = canvas.scene

#axis = scene.visuals.XYZAxis(parent=view.scene)

#cam = scene.cameras.TurntableCamera(parent=view.scene, fov=60., name='Turntable')

#view.camera = cam

program = gloo.Program(vertex_source, fragment_source)
