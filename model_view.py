from PySide6.QtCore import QAbstractListModel, Qt

class StringListModel(QAbstractListModel):
    def __init__(self, strings, parent=None):
###
        super().__init__(parent)
        self._strings = strings

    def data(self, index, role):
        row = index.row()
        if not index.isValid() or row >= len(self._strings):
            return None

        if role != Qt.DisplayRole and role != Qt.EditRole:
            return None

        return self._strings[row]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return f"Column {section}"

        return f"Row {section}"
