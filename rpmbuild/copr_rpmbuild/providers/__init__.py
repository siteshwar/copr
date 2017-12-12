from ..helpers import SourceType
from .rubygems import RubyGemsProvider
from .pypi import PyPIProvider
from .spec import SpecUrlProvider
from .scm import ScmProvider
from .custom import CustomProvider


__all__ = [RubyGemsProvider, PyPIProvider,
           SpecUrlProvider, ScmProvider]


def factory(source_type):
    try:
        return {
            SourceType.LINK: SpecUrlProvider,
            SourceType.UPLOAD: SpecUrlProvider,
            SourceType.RUBYGEMS: RubyGemsProvider,
            SourceType.PYPI: PyPIProvider,
            SourceType.SCM: ScmProvider,
            SourceType.CUSTOM: CustomProvider,
        }[source_type]
    except KeyError:
        raise RuntimeError("No provider associated with this source type")
