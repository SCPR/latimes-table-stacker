from table_stacker.models import Table
from bakery.views import BuildableDetailView, BuildableListView, BuildableTemplateView
import logging

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

class TableListView(BuildableListView):
    """
    A list of all tables.
    """
    queryset = Table.live.all()


class TableDetailView(BuildableDetailView):
    """
    All about one table.
    """
    queryset = Table.live.all()

    def get_context_data(self, **kwargs):
        context = super(TableDetailView, self).get_context_data(**kwargs)
        table = context['object'].get_tablefu()
        context.update({
            'size_choices': [1,2,3,4],
            'table': table
        })

        return context
