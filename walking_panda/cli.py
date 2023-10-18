from . import panda

import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--scale", type=int, help="Scale Panda Size",
                        )
    parser.add_argument("--scale-nature", type=float, help="Scale Nature Size",
                        )
    parser.add_argument("--nature-position", type=str, help="Change Nature Position",
                        choices=['left', 'right'],
                        )
    parser.add_argument("--panda-jogging", type=float, help="Panda Speed Control",
                        )
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
