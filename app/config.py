from typing import List, Mapping, Union

import attr
import toml
import pathlib

CUR_DIR = pathlib.Path(__file__).parent
CONFIG_PATH = CUR_DIR.joinpath('config.toml')


@attr.s
class Config(object):
    access_token: str = attr.ib()
    admin_peers: List[str] = attr.ib()

    @classmethod
    def from_toml(
            cls,
            toml: Mapping[str, Union[str, List[str]]]
    ):
        return cls(
            access_token=toml["access_token"],
            admin_peers=toml["admin_peers"]
        )


def load_config() -> Config:
    return Config.from_toml(toml.load(CONFIG_PATH))


CONFIG = load_config()
