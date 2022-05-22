spin = input()
electric = input()
particles = ['Strange', 'Charm', 'Electron', 'Neutrino', 'Photon']
classes = ['Quark', 'Lepton', 'Boson']
if spin == '1/2':
    if electric == '-1/3':
        print(particles[0], classes[0])
    elif electric == '2/3':
        print(particles[1], classes[0])
    elif electric == '-1':
        print(particles[2], classes[1])
    else:
        print(particles[3], classes[1])
else:
    print(particles[4], classes[2])
