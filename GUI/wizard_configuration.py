from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import form_wizard_page_1
import form_wizard_page_2
import form_wizard_page_3
import form_wizard_page_4
import form_wizard_page_5
import form_wizard_page_6
import form_wizard_page_7
import form_wizard_page_8
import Source_tree
import Receiver_tree
import xml.dom.minidom as xml_format
import os
import pandas as pd
import Core.DAO.DB_connector as db_con
from Logger import Logger
from alarm_window import show_alarm_window
from Validate import Validate_res
from Core.DAO import XML_DAO as xpc
from alarm_window import show_alarm_window
from error_window import show_error_window
import source_column_editor_viewer
import target_column_editor_viewer
import copy
import Dict_tree



class WizardConfig(QtWidgets.QWizard):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setPage(RoadMapConfiguration.db_parameters_and_check_mode, Page1(self))
        self.setPage(RoadMapConfiguration.target_table_and_db_schema, Page2(self))
        self.setPage(RoadMapConfiguration.source_columns, Page3(self))
        self.setPage(RoadMapConfiguration.receiver_columns, Page4(self))
        self.setPage(RoadMapConfiguration.dictionary, Page5(self))
        self.setPage(RoadMapConfiguration.final_page, Page6(self))
        # self.setPage(RoadMapConfiguration.DictColumnsParameters, Page7(self))
        # self.setPage(RoadMapConfiguration.DictTables, Page8(self))

        self.resize(900, 550)


class Page1(QtWidgets.QWizardPage, form_wizard_page_1.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loggerInst = Logger.Log_info.getInstance()

        self.pref = {'col_to_check': []}
        self.setupUi(self)

        self.open_excel_file = QtWidgets.QToolButton(self.horizontalLayoutWidget_3)
        self.open_excel_file.setObjectName("open_excel_file")
        self.horizontalLayout_3.addWidget(self.open_excel_file)
        self.open_excel_file.setText("...")

        self.registerField('dictionary_state', self.checkBox_Dictionary)
        self.registerField('lineEdit_dbtype', self.lineEdit_dbtype)
        self.registerField('lineEdit_dbhost', self.lineEdit_dbhost)
        self.registerField('lineEdit_dbuser', self.lineEdit_dbuser)
        self.registerField('lineEdit_dbpass', self.lineEdit_dbpass)
        self.registerField('lineEdit_dbbase', self.lineEdit_dbbase)
        self.registerField('lineEdit_dbport', self.lineEdit_dbport)
        self.registerField('comboBox_chose_loadMode', self.comboBox_chose_loadMode)
        self.registerField('excelFileName', self.excelFileName)
        self.registerField('checkBox_checkMode', self.checkBox_checkMode)
        self.registerField('checkBox_both', self.checkBox_both)
        self.registerField('compare_file', self.compare_file)

        self.df_compare = None


        self.lineEdit_dbtype.addItems(['mysql', 'mssql'])
        self.comboBox_chose_loadMode.addItems(['insert', 'update'])

        self.treeWidget_linked_columns = TreeWidgetLinkedColumns(widget_sighal=self.excelFileName, pref_dict=self.pref)
        self.tree_widget_box.addWidget(self.treeWidget_linked_columns)
        self.treeWidget_linked_columns.setHeaderLabels(['Linked Columns', 'Target columns'])
        self.treeWidget_linked_columns.setColumnCount(2)

        self.comboBox_list_source_excel = comboBox_list_for_Page2(
            self.horizontalLayoutWidget_3,
            check_widget=self.treeWidget_linked_columns
        )

        self.comboBox_list_source_excel.setObjectName("comboBox_list_source_excel")
        self.horizontalLayout_3.addWidget(self.comboBox_list_source_excel)
        self.comboBox_list_source_excel.installEventFilter(ev_filt(parent=self.comboBox_list_source_excel))

        self.comboBox_set_list_checked = comboBox_list_for_Page2(
            self.horizontalLayoutWidget_5,
            check_widget=self.treeWidget_linked_columns
        )

        self.comboBox_set_list_checked.setObjectName("comboBox_set_list_checked")
        self.horizontalLayout_5.addWidget(self.comboBox_set_list_checked)
        self.comboBox_set_list_checked.installEventFilter(ev_filt(parent=self.comboBox_set_list_checked))

        self.label_check_mode.setDisabled(False)
        self.label_check_mode.setDisabled(True)
        self.open_excel_compare_file.setDisabled(True)
        self.compare_file.setDisabled(True)
        self.comboBox_set_list_checked.setDisabled(True)
        self.checkBox_Dictionary.setDisabled(False)
        self.treeWidget_linked_columns.setDisabled(True)
        self.checkBox_both.setDisabled(True)
        self.compare_file.setDisabled(True)

        self.open_excel_file.clicked.connect(self.open_excel_folder)
        self.open_excel_compare_file.clicked.connect(self.open_excel_compare_folder)
        self.checkBox_checkMode.stateChanged.connect(self.add_asterisc_checkBox_checkMode)

        self.treeWidget_linked_columns.actionAddColumn.triggered.connect(self.add_link_col)
        self.treeWidget_linked_columns.actionDeleteColumn.triggered.connect(self.delete_link_col)
        self.comboBox_list_source_excel.currentIndexChanged.connect(self.add_asterisc_label_receiver)
        self.comboBox_set_list_checked.currentIndexChanged.connect(self.add_asterisc_checkMode)
        self.excelFileName.textChanged.connect(self.add_asterisc_label_receiver)
        self.compare_file.textChanged.connect(self.add_asterisc_checkMode)

    #
        self.lineEdit_dbhost.setText('localhost')
        self.lineEdit_dbpass.setText('P@$$w0rd')
        self.lineEdit_dbport.setText('3306')
        self.lineEdit_dbuser.setText('root')
        self.lineEdit_dbbase.setText('designer_etl')
    #

    def add_asterisc_checkMode(self):

        while self.treeWidget_linked_columns.topLevelItemCount() > 0:
            self.treeWidget_linked_columns.takeTopLevelItem(0)

    def add_asterisc_label_receiver(self):
        while self.treeWidget_linked_columns.topLevelItemCount() > 0:
            self.treeWidget_linked_columns.takeTopLevelItem(0)

    def add_asterisc_checkMode(self):

        while self.treeWidget_linked_columns.topLevelItemCount() > 0:
            self.treeWidget_linked_columns.takeTopLevelItem(0)


    def add_asterisc_label_receiver(self):
        while self.treeWidget_linked_columns.topLevelItemCount() > 0:
            self.treeWidget_linked_columns.takeTopLevelItem(0)

    def add_link_col(self):
        self.registerField('tree_widget_box_link_columns', self.treeWidget_linked_columns)

        if self.df_compare:
            target_column = [i for i in self.df_compare.parse(self.comboBox_set_list_checked.currentIndex()).columns.values]
        else:
            show_alarm_window(self, "Choose a file !!!")
            return

        source_column = [i for i in self.df.parse(self.comboBox_list_source_excel.currentIndex()).columns.values]

        row_check = LinkedColumns(
            tree_widget=self.treeWidget_linked_columns,
            parent=self.treeWidget_linked_columns,
            target_columns=target_column,
            source_columns=source_column,
            current_column=None)
        self.treeWidget_linked_columns.addTopLevelItem(row_check)

        self.pref['col_to_check'].append(row_check)

    def delete_link_col(self):
        self.pref['col_to_check'].remove(self.treeWidget_linked_columns.currentItem())
        self.treeWidget_linked_columns.takeTopLevelItem(
            self.treeWidget_linked_columns.indexFromItem(self.treeWidget_linked_columns.currentItem()).row())

    def open_excel_folder(self):

        path_name = QtWidgets.QFileDialog.getOpenFileName(directory=os.path.join(os.getcwd(), '..', 'Source'),
                                                          filter='*.xlsx')
        path = os.path.basename(path_name[0])
        if path:

            if self.treeWidget_linked_columns.topLevelItemCount() > 0 or self.wizard().page(2).treeWidget_of_Source.topLevelItemCount() > 0:
                result = QtWidgets.QMessageBox.question(self,
                                                        "Change file ?",
                                                        "Change file ? Linked columns and Source Columns will remove",
                                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                        QtWidgets.QMessageBox.No
                                                        )

                if result == QtWidgets.QMessageBox.Yes:
                    self.excelFileName.setText(path)
                    pathToExcel = os.path.join(os.path.join(os.getcwd(), '..', 'Source'), path)
                    self.df = pd.ExcelFile(pathToExcel)
                    self.comboBox_list_source_excel.clear()
                    self.comboBox_list_source_excel.addItems([i for i in self.df.sheet_names])
                    self.excelFileName.textChanged.emit(path)
                    self.comboBox_list_source_excel.currentIndexChanged.emit(0)
            else:
                self.excelFileName.setText(path)
                pathToExcel = os.path.join(os.path.join(os.getcwd(), '..', 'Source'), path)
                self.df = pd.ExcelFile(pathToExcel)
                self.comboBox_list_source_excel.clear()
                self.comboBox_list_source_excel.addItems([i for i in self.df.sheet_names])
                self.excelFileName.textChanged.emit(path)
                self.comboBox_list_source_excel.currentIndexChanged.emit(0)

    def open_excel_compare_folder(self):

        path_name_compare_excel = QtWidgets.QFileDialog.getOpenFileName(directory=os.path.join(os.getcwd(), '..', 'Source'),
                                                          filter='*.xlsx')
        path_compare_excel = os.path.basename(path_name_compare_excel[0])

        if path_compare_excel:
            self.path_name_compare_excel = path_name_compare_excel[0]
            self.path_compare_excel = path_compare_excel

            if self.treeWidget_linked_columns.topLevelItemCount() > 0:
                result = QtWidgets.QMessageBox.question(self,
                                                                "Change file ?",
                                                                "Change file ? Linked columns will remove",
                                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                                QtWidgets.QMessageBox.No
                                                                )

                if result == QtWidgets.QMessageBox.Yes:
                    self.compare_file.setText(path_compare_excel)
                    pathToExcel = os.path.join(os.path.join(os.getcwd(), '..', 'Source'),
                                               path_compare_excel)
                    self.df_compare = pd.ExcelFile(pathToExcel)
                    self.comboBox_set_list_checked.clear()
                    self.comboBox_set_list_checked.addItems([i for i in self.df_compare.sheet_names])
                    self.compare_file.textChanged.emit(path_compare_excel)
                    self.comboBox_set_list_checked.currentIndexChanged.emit(0)
            else:
                self.compare_file.setText(path_compare_excel)
                pathToExcel = os.path.join(os.path.join(os.getcwd(), '..', 'Source'),
                                           path_compare_excel)
                self.df_compare = pd.ExcelFile(pathToExcel)
                self.comboBox_set_list_checked.clear()
                self.comboBox_set_list_checked.addItems([i for i in self.df_compare.sheet_names])
                self.compare_file.textChanged.emit(path_compare_excel)
                self.comboBox_set_list_checked.currentIndexChanged.emit(0)

    def add_asterisc_checkBox_checkMode(self):
        if self.checkBox_checkMode.isChecked():
            self.label_check_mode.setDisabled(True)
            self.label_check_mode.setDisabled(False)
            self.open_excel_compare_file.setDisabled(False)
            self.compare_file.setDisabled(False)
            self.comboBox_set_list_checked.setDisabled(False)
            self.checkBox_Dictionary.setDisabled(True)
            self.checkBox_Dictionary.setChecked(False)
            self.treeWidget_linked_columns.setDisabled(False)
            self.checkBox_both.setDisabled(False)
            self.compare_file.setDisabled(False)

        else:
            self.compare_file.setDisabled(True)
            self.label_check_mode.setDisabled(False)
            self.label_check_mode.setDisabled(True)
            self.open_excel_compare_file.setDisabled(True)
            self.compare_file.setDisabled(True)
            self.comboBox_set_list_checked.setDisabled(True)
            self.checkBox_Dictionary.setDisabled(False)
            self.treeWidget_linked_columns.setDisabled(True)
            self.checkBox_both.setDisabled(True)

    def validatePage(self) -> bool:

        if not self.excelFileName.text():
            show_alarm_window(self, "Choose a source file !!!")
            return False
        else:
            con = db_con.Connection.get_instance(self.loggerInst)
            try:
                con.connectToTheDB(host=self.lineEdit_dbhost.text(),
                                   user=self.lineEdit_dbuser.text(),
                                   password=self.lineEdit_dbpass.text(),
                                   dbname=self.lineEdit_dbbase.text(),
                                   port=int(self.lineEdit_dbport.text()),
                                   dbtype=self.lineEdit_dbtype.currentText()
                                   )
                con.test_conn()

            except Exception:
                show_alarm_window(self, "Can't connect to the DB !!!")
                return False
            else:
                self.con = con
                return True

    def close_project_data(self):

        self.pref = {}



class Page2(QtWidgets.QWizardPage, form_wizard_page_2.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.adjustSize()


        self.comboBox_dbSchema = comboBox_list_for_Page3(self.verticalLayoutWidget)
        self.comboBox_dbSchema.setObjectName("comboBox_dbSchema")
        self.horizontalLayout_16.addWidget(self.comboBox_dbSchema)

        self.target_table_name = comboBox_list_for_Page3(self.verticalLayoutWidget)
        self.target_table_name.setObjectName("target_table_name")
        self.horizontalLayout_14.addWidget(self.target_table_name)


    def initializePage(self) -> None:

        self.comboBox_dbSchema.addItems(sorted([i[0] for i in Validate_res.Validate.queryForSchemasInDb_edit(
            dbtype=self.wizard().page(0).lineEdit_dbtype.currentText(),
            connector=self.wizard().page(0).con,
            executor=Validate_res.Validate.executor,
            cur=self.wizard().page(0).con.cursor,
            loggerInst=self.wizard().page(0).loggerInst
        )]))

        self.target_table_name.addItems(sorted([i[0] for i in Validate_res.Validate.queryForTableInDbList_edit(
            connector=self.wizard().page(0).con,
            dbtype=self.wizard().page(0).lineEdit_dbtype.currentText(),
            executor=Validate_res.Validate.executor,
            cur=self.wizard().page(0).con.cursor,
            loggerInst=self.wizard().page(0).loggerInst
        )]))




class Page3(QtWidgets.QWizardPage, form_wizard_page_3.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.dict_pref = {
            'dictTableName': None,
            'indxDbColumn': None,
            'indxColumnDic': None,
            'colType': '---',
            'arrOfDictColumns': None,
            'colName': None,
            'colNameDb': None,
            'cropEnd_mode': 'false',
            'addValueEnd_mode': 'false',
            'takeFromBegin_mode': 'false',
            'cropBegin_mode': 'false',
            'addValueBegin_mode': 'false',
            'addValueBoth_mode': 'false',
            'replace_mode': 'false',
            'isPK': 'false',
            'filter_mode': 'false',
            'post_filter_mode': 'false'
        }

        self.list_of_source_cols_links = []

        self.treeWidget_of_Source = Source_tree.Source_tree()
        self.horizontalLayout.addWidget(self.treeWidget_of_Source)
        self.treeWidget_of_Source.actionDuplicateColumn.triggered.connect(self.addColumnField)
        self.treeWidget_of_Source.actionDuplicateReplace.triggered.connect(self.duplicateReplace)
        self.treeWidget_of_Source.actionDeleteColumn.triggered.connect(self.deleteColumn)
        self.treeWidget_of_Source.actionDeleteReplace.triggered.connect(self.deleteReplace)



    def initializePage(self) -> None:

        if not hasattr(self, "filter_db"):
            self.filter_db = ev_filt_of_Page3(parent=self.wizard().page(1).comboBox_dbSchema)
        if not hasattr(self, "filter_target"):
            self.filter_target = ev_filt_of_Page3(parent=self.wizard().page(1).target_table_name)

        self.colnames_in_receiver = [i[0] for i in Validate_res.Validate.queryForColumns_edit(
            dbtype=self.wizard().page(0).lineEdit_dbtype.currentText(),
            target_table=self.wizard().page(1).target_table_name.currentText(),
            db_base=self.wizard().page(1).comboBox_dbSchema.currentText(),
            connector=self.wizard().page(0).con,
            executor=Validate_res.Validate.executor,
            cur=self.wizard().page(0).con.cursor,
            loggerInst=self.wizard().page(0).loggerInst
        )]

        self.columns_in_source = [i for i in self.wizard().page(0).df.parse(self.wizard().page(0).comboBox_list_source_excel.currentIndex()).columns.values]

    def deleteReplace(self):
        cur_column = list(filter(lambda x: x['colName'].combo_box_name.currentText() ==
                                           self.treeWidget_of_Source.currentItem().parent().combo_box_name.currentText(),
                                 self.list_of_source_cols_links))[0]
        if len(cur_column['replace_box']) > 1:
            cur_column['replace_box'].remove(self.treeWidget_of_Source.currentItem())
        else:
            show_alarm_window(self, "You can't delete last element !!!")
            return

        self.treeWidget_of_Source.currentItem().parent().takeChild(
            self.treeWidget_of_Source.indexFromItem(self.treeWidget_of_Source.currentItem()).row())

    def deleteColumn(self):
        if len(self.list_of_source_cols_links) > 1:
            element = list(filter(lambda x: x['colName'].combo_box_name.currentText() == self.treeWidget_of_Source.currentItem().combo_box_name.currentText(), self.list_of_source_cols_links))[0]
            self.list_of_source_cols_links.remove(element)
            self.treeWidget_of_Source.takeTopLevelItem(self.treeWidget_of_Source.indexFromItem(self.treeWidget_of_Source.currentItem()).row())
        else:
            show_alarm_window(self, "You can't delete last element !!!")
            return

    def duplicateReplace(self):
        replace = source_column_editor_viewer.ReplaceRow(column_property=self.dict_pref,
                                                         parent=self.treeWidget_of_Source,
                                                         parent_widget=self.treeWidget_of_Source.currentItem().parent(),
                                                         after_widget=self.treeWidget_of_Source.currentItem())

        self.treeWidget_of_Source.addTopLevelItem(replace)
        list(filter(lambda x: x['colName'].combo_box_name.currentText() ==
                              self.treeWidget_of_Source.currentItem().parent().combo_box_name.currentText(),
                    self.list_of_source_cols_links))[0]['replace_box'].append(replace)

    def cleanupPage(self) -> None:
        self.wizard().page(1).comboBox_dbSchema.removeEventFilter(self.filter_db)
        self.wizard().page(1).target_table_name.removeEventFilter(self.filter_target)

        self.wizard().page(1).comboBox_dbSchema.check_widget = self.treeWidget_of_Source
        self.wizard().page(1).target_table_name.check_widget = self.treeWidget_of_Source
        self.wizard().page(0).comboBox_list_source_excel.widget_to_delete_sources = self.treeWidget_of_Source
        self.wizard().page(1).target_table_name.widget_to_delete_target_tables = self.wizard().page(3).treeWidget_of_Receiver

        self.wizard().page(1).comboBox_dbSchema.currentIndexChanged.connect(self.clear)
        self.wizard().page(1).target_table_name.currentIndexChanged.connect(self.clear)
        self.wizard().page(0).excelFileName.textChanged.connect(self.clear)
        self.wizard().page(0).comboBox_list_source_excel.currentIndexChanged.connect(self.clear)

        self.wizard().page(1).comboBox_dbSchema.installEventFilter(self.filter_db)
        self.wizard().page(1).target_table_name.installEventFilter(self.filter_target)


    def clear(self):
        while self.treeWidget_of_Source.topLevelItemCount() > 0:
            self.treeWidget_of_Source.takeTopLevelItem(0)
        self.list_of_source_cols_links = []


    def addColumnField(self):
        source_column_editor_viewer.create_input_column(
            tree_table=self.treeWidget_of_Source,
            db_colnames=self.colnames_in_receiver,
            column_property=self.dict_pref,
            list_of_cols=self.list_of_source_cols_links,
            indx=self.treeWidget_of_Source.indexFromItem(self.treeWidget_of_Source.currentItem()).row(),
            source_columnes=self.columns_in_source
            )



class Page4(QtWidgets.QWizardPage, form_wizard_page_4.Ui_Form):
    column_prop_template = {
        'colName': None,
        'fromExcel': 'false',
        'defaultValue': None,
        'defaultValue_mode': 'false',
        'colType': 'str',
        'ifNull': None,
        'ifNull_mode': 'false',
        'isAutoInc': 'false',
        'isConc': 'false',
        'isUpdateCondition': 'false',
        'fromDb': 'false'
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.treeWidget_of_Receiver = Receiver_tree.Receiver_tree()
        self.horizontalLayout.addWidget(self.treeWidget_of_Receiver)

        self.list_of_receiver_cols_links = []


    def initializePage(self) -> None:
        self.clear()
        for col in self.wizard().page(2).colnames_in_receiver:
            col_prop = copy.deepcopy(self.column_prop_template)
            col_prop['colName'] = f'{col}'

            target_column_editor_viewer.create_receiver_column(
                tree_table=self.treeWidget_of_Receiver,
                column_property=col_prop,
                list_of_cols=self.list_of_receiver_cols_links
            )

    def clear(self):
        while self.treeWidget_of_Receiver.topLevelItemCount() > 0:
            self.treeWidget_of_Receiver.takeTopLevelItem(0)

    # def cleanupPage(self) -> None:



    def nextId(self) -> int:
        if self.field('dictionary_state'):
            return RoadMapConfiguration.dictionary
        else:
            return RoadMapConfiguration.final_page

class Page5(QtWidgets.QWizardPage, form_wizard_page_5.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.list_of_dict_pref = []
        self.config_dict = {}
        self.validator = Validate_res

    def initializePage(self) -> None:
        self.tables_in_receiver = [i[0] for i in Validate_res.Validate.queryForTableInDbList_edit(
            connector=self.wizard().page(0).con,
            dbtype=self.wizard().page(0).lineEdit_dbtype.currentText(),
            executor=Validate_res.Validate.executor,
            cur=self.wizard().page(0).con.cursor,
            loggerInst=self.wizard().page(0).loggerInst
        )]

        self.columns_in_source = self.wizard().page(2).columns_in_source

        self.tree_dict = Dict_tree.DictTree(
            list_of_dict_pref=self.list_of_dict_pref,
            config=self.config_dict,
            validator=self.validator,
            tables_in_receiver=self.tables_in_receiver,
            columns_names_source=self.columns_in_source,
        )

        self.horizontalLayout.addWidget(self.tree_dict)






class Page6(QtWidgets.QWizardPage, form_wizard_page_6.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent




class RoadMapConfiguration(QtWidgets.QWizard):

    db_parameters_and_check_mode = 0
    target_table_and_db_schema = 1
    source_columns = 2
    receiver_columns = 3
    dictionary = 4
    final_page = 5
    # DictColumnsParameters = 6
    # DictTables = 7


class TreeWidgetLinkedColumns(QtWidgets.QTreeWidget):
    def __init__(self, parent=None, widget_sighal=None, pref_dict=None):
        super().__init__(parent)

        self.pref = pref_dict
        self.widget_sighal = widget_sighal
        self.treeWidget_linked_columns = QtWidgets.QTreeWidget()
        self.treeWidget_linked_columns.setGeometry(QtCore.QRect(10, 260, 271, 101))
        self.treeWidget_linked_columns.setObjectName("treeWidget_linked_columns")
        self.treeWidget_linked_columns.headerItem().setText(0, "1")

        self.context_menu_add_row = QtWidgets.QMenu()
        self.actionAddColumn = QtWidgets.QAction()
        self.actionDeleteColumn = QtWidgets.QAction()
        self.actionAddColumn.setText("Add Column")
        self.actionDeleteColumn.setText("Delete Column")
        self.context_menu_add_row.addAction(self.actionAddColumn)
        self.context_menu_add_row.addAction(self.actionDeleteColumn)
        self.widget_sighal.textChanged.connect(self.delete_columns)

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        self.context_menu_add_row.exec(event.globalPos())

    def delete_columns(self):
        while self.topLevelItemCount() > 0:
            self.takeTopLevelItem(0)


class comboBox_list_for_Page2(QtWidgets.QComboBox):
    def __init__(self, parent=None, check_widget=None, widget_to_delete_target_tables=None):
        super().__init__(parent)
        self.check_widget = check_widget
        self.widget_to_delete_target_tables = widget_to_delete_target_tables


class comboBox_list_for_Page3(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)



class ev_filt(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def eventFilter(self, a0, a1) -> bool:
        if a1.type() == QtCore.QEvent.MouseButtonPress:
            if self.parent().check_widget.topLevelItemCount() > 0 or \
                    (hasattr(self.parent(), "widget_to_delete_sources") and self.parent().widget_to_delete_sources.topLevelItemCount() > 0):
                result = QtWidgets.QMessageBox.question(None,
                                                        "Change list ?",
                                                        "Change list ? Linked and Source Columns will remove",
                                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                        QtWidgets.QMessageBox.No
                                                        )

                if result == QtWidgets.QMessageBox.No:
                    return True
                elif result == QtWidgets.QMessageBox.Yes:
                    return False
            else:
                return False
        else:
            return QtCore.QObject.eventFilter(self, a0, a1)



class ev_filt_of_Page3(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        if a1.type() == QtCore.QEvent.MouseButtonPress:
            if (hasattr(self.parent(), "check_widget") and self.parent().check_widget.topLevelItemCount() > 0) or\
                    (hasattr(self.parent(), "widget_to_delete_target_tables") and self.parent().widget_to_delete_target_tables.topLevelItemCount() > 0):
                result = QtWidgets.QMessageBox.question(None,
                                                        "Change ?",
                                                        "Change ? Source and Target columns will remove",
                                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                        QtWidgets.QMessageBox.No
                                                        )

                if result == QtWidgets.QMessageBox.No:
                    return True
                elif result == QtWidgets.QMessageBox.Yes:
                    return False
            else:
                return False
        else:
            return QtCore.QObject.eventFilter(self, a0, a1)


class LinkedColumns(QtWidgets.QTreeWidgetItem):
    def __init__(self, tree_widget: QtWidgets.QTreeWidget, current_column, parent, target_columns, source_columns):
        super().__init__(parent, ['', ])

        self.combo_box_source_links = QtWidgets.QComboBox()
        self.combo_box_target_links = QtWidgets.QComboBox()

        self.combo_box_source_links.addItems(source_columns)
        self.combo_box_target_links.addItems(target_columns)

        if current_column: # если есть колонка из которой создается
            self.combo_box_source_links.setCurrentIndex(source_columns.index(current_column['colNameInSource']))
            self.combo_box_target_links.setCurrentIndex(target_columns.index(current_column['linkedColName']))

        tree_widget.setItemWidget(self, 0, self.combo_box_source_links)
        tree_widget.setItemWidget(self, 1, self.combo_box_target_links)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = WizardConfig(app)
    w.show()
    sys.exit(app.exec())