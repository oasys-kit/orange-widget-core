#import pkg_resources
import importlib_metadata, importlib_resources

from orangecanvas import config

from . import discovery
from . import workflow

WIDGETS_ENTRY = "orange.widgets"
ADDONS_ENTRY = "orange.addon"


class orangeconfig(config.default):
    @staticmethod
    def widgets_entry_points():
        """
        Return an `EntryPoint` iterator for all 'orange.widget' entry
        points plus the default Orange Widgets.

        """
        #dist = pkg_resources.get_distribution("Orange")
        #ep = pkg_resources.EntryPoint("Orange Widgets", "Orange.widgets",
        #                              dist=dist)

        dist = importlib_metadata.distribution("Orange")
        ep = importlib_metadata.EntryPoint(name="Orange Widgets", value="Orange.widgets", group=dist.name)

        #return iter((ep,) + tuple(pkg_resources.iter_entry_points(WIDGETS_ENTRY)))
        return iter((ep,) + tuple(importlib_metadata.entry_points(group=WIDGETS_ENTRY)))

    @staticmethod
    def addon_entry_points():
        #return pkg_resources.iter_entry_points(ADDONS_ENTRY)
        return importlib_metadata.entry_points(group=ADDONS_ENTRY)

    @staticmethod
    def addon_pypi_search_spec():
        return {"keywords": ["orange3 add-on"]}

    widget_discovery = discovery.WidgetDiscovery
    workflow_constructor = workflow.WidgetsScheme
