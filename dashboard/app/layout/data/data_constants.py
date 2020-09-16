#!/usr/bin/env python3

from collections import namedtuple

RepresentableKey = namedtuple('RepresentableKey', 'key description')

class DataConstants(object):

    @staticmethod
    def repo_placeholder() -> str:
        return "__repo_placeholder__"

    @staticmethod
    def app_name() -> RepresentableKey:
        return RepresentableKey('app_name', 'App name')

    @staticmethod
    def size_type() -> RepresentableKey:
        return RepresentableKey('size_type', 'Kind of size')    

    @staticmethod
    def size_in_mb() -> RepresentableKey:
        return RepresentableKey('size_in_mb', 'Size in MB')

    @staticmethod
    def date() -> RepresentableKey:
        return RepresentableKey('date', 'Sampling date')

    @staticmethod
    def kloc() -> RepresentableKey:
        return RepresentableKey('kloc', 'K-Lines Of Code (kLOC)')

    @staticmethod
    def n_of_deps() -> RepresentableKey:
        return RepresentableKey('n_of_deps', 'Number of dependencies')

    @staticmethod
    def deps_test_loc() -> RepresentableKey:
        return RepresentableKey('deps_test_loc', 'Dependencies Tests LOC')

    @staticmethod
    def deps_prod_loc() -> RepresentableKey:
        return RepresentableKey('deps_prod_loc', 'Dependencies Production LOC')

    @staticmethod
    def repo_test_loc() -> RepresentableKey:
        return RepresentableKey('repo_test_loc', f'{DataConstants.repo_placeholder()} Tests LOC')

    @staticmethod
    def repo_prod_loc() -> RepresentableKey:
        return RepresentableKey('repo_prod_loc', f'{DataConstants.repo_placeholder()} Production LOC')

    @staticmethod
    def repo_dupl_loc() -> RepresentableKey:
        return RepresentableKey('repo_dupl_loc', f'{DataConstants.repo_placeholder()} Duplicated LOC')

    @staticmethod
    def internal_deps() -> RepresentableKey:
        return RepresentableKey('internal_deps', 'N. of internal dependencies')

    @staticmethod
    def external_deps() -> RepresentableKey:
        return RepresentableKey('external_deps', 'N. of external dependencies')