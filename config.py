from typing import List, Mapping, Union

import attr
import toml


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
    return Config.from_toml(toml.load('config.toml'))


CONFIG = load_config()
