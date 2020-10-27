# Copyright (C) 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

import argparse

from ..util.project import load_project


def build_parser(parser_ctor=argparse.ArgumentParser):
    parser = parser_ctor()

    parser.add_argument('rev', help="Commit or tag")
    parser.add_argument('-s', '--soft', action='store_true',
        help="Don't update working tree")
    parser.add_argument('-p', '--project', dest='project_dir', default='.',
        help="Directory of the project to operate on (default: current dir)")
    parser.set_defaults(command=commit_command)

    return parser

def commit_command(args):
    project = load_project(args.project_dir)

    project.vcs.checkout(args.rev, update_data=not args.soft)

    return 0