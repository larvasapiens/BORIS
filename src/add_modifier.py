#!/usr/bin/env python3

"""
BORIS
Behavioral Observation Research Interactive Software
Copyright 2012-2019 Olivier Friard

This file is part of BORIS.

  BORIS is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  any later version.

  BORIS is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not see <http://www.gnu.org/licenses/>.

"""



from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from add_modifier_ui5 import Ui_Dialog

import copy
import dialog
from config import *
from utilities import sorted_keys


class addModifierDialog(QDialog, Ui_Dialog):

    tabMem = -1
    itemPositionMem = -1

    def __init__(self, modifiers_str, subjects=[], parent=None):

        super().__init__()
        self.setupUi(self)

        self.subjects = subjects

        self.pbAddModifier.clicked.connect(self.addModifier)
        self.pbAddModifier.setIcon(QIcon(":/frame_forward"))
        self.pbAddSet.clicked.connect(self.addSet)
        self.pbRemoveSet.clicked.connect(self.removeSet)
        self.pbModifyModifier.clicked.connect(self.modifyModifier)
        self.pbModifyModifier.setIcon(QIcon(":/frame_backward"))

        self.pbMoveUp.clicked.connect(self.moveModifierUp)
        self.pbMoveDown.clicked.connect(self.moveModifierDown)
        self.pbMoveSetLeft.clicked.connect(self.moveSetLeft)
        self.pbMoveSetRight.clicked.connect(self.moveSetRight)
        self.pbRemoveModifier.clicked.connect(self.removeModifier)
        self.pb_add_subjects.clicked.connect(self.add_subjects)

        self.pbOK.clicked.connect(self.accept)
        self.pbCancel.clicked.connect(self.reject)

        self.leSetName.textChanged.connect(self.set_name_changed)

        self.cbType.currentIndexChanged.connect(self.type_changed)

        dummy_dict = eval(modifiers_str) if modifiers_str else {}
        modif_values = []
        for idx in sorted_keys(dummy_dict):
            modif_values.append(dummy_dict[idx])

        self.modifiers_sets_dict = {}
        for modif in modif_values:
            self.modifiers_sets_dict[str(len(self.modifiers_sets_dict))] = copy.deepcopy(modif)

        self.tabWidgetModifiersSets.currentChanged.connect(self.tabWidgetModifiersSets_changed)

        # create tab
        for idx in sorted_keys(self.modifiers_sets_dict):
            self.tabWidgetModifiersSets.addTab(QWidget(), f"Set #{int(idx) + 1}")

        if self.tabWidgetModifiersSets.currentIndex() == -1:
            for w in [self.lbSetName, self.lbType, self.lbValues, self.leSetName, self.cbType, self.lwModifiers, self.pbMoveUp,
                      self.pbMoveDown, self.pbRemoveModifier, self.pbRemoveSet, self.pbMoveSetLeft, self.pbMoveSetRight,
                      ]:
                w.setVisible(False)
            for w in [self.leModifier, self.leCode, self.pbAddModifier, self.pbModifyModifier, self.pb_add_subjects]:
                w.setEnabled(False)

        # set first tab as active
        self.tabMem = 0


    def add_subjects(self):
        """
        add subjects as modifiers
        """

        for subject in self.subjects:
            if self.itemPositionMem != -1:
                self.lwModifiers.insertItem(self.itemPositionMem, subject)
            else:
                self.lwModifiers.addItem(subject)

        self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]["values"] = [self.lwModifiers.item(x).text()
                                                                                               for x in range(self.lwModifiers.count())]


    def set_name_changed(self):
        """
        set name changed
        """
        if not self.modifiers_sets_dict:
            self.modifiers_sets_dict["0"] = {"name": "", "type": SINGLE_SELECTION, "values": []}
        self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]["name"] = self.leSetName.text().strip()


    def type_changed(self):
        """
        type changed
        """
        if not self.modifiers_sets_dict:
            self.modifiers_sets_dict["0"] = {"name": "", "type": SINGLE_SELECTION, "values": []}
        self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]["type"] = self.cbType.currentIndex()
        # disable if modifier numeric
        for obj in [self.lbValues, self.lwModifiers, self.leModifier, self.leCode, self.lbModifier, self.lbCode, self.lbCodeHelp,
                    self.pbMoveUp, self.pbMoveDown, self.pbRemoveModifier, self.pb_add_subjects,
                    self.pbAddModifier, self.pbModifyModifier]:
            obj.setEnabled(self.cbType.currentIndex() != NUMERIC_MODIFIER)


    def moveSetLeft(self):
        """
        move selected modifiers set left
        """
        if self.tabWidgetModifiersSets.currentIndex():
            self.modifiers_sets_dict[
                str(self.tabWidgetModifiersSets.currentIndex() - 1)
            ], self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())] = (
                dict(self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]),
                dict(self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex() - 1)]),
            )
            self.tabWidgetModifiersSets.setCurrentIndex(self.tabWidgetModifiersSets.currentIndex() - 1)
            self.tabMem = self.tabWidgetModifiersSets.currentIndex()


    def moveSetRight(self):
        """
        move selected modifiers set right
        """
        if self.tabWidgetModifiersSets.currentIndex() < self.tabWidgetModifiersSets.count() - 1:

            self.modifiers_sets_dict[
                str(self.tabWidgetModifiersSets.currentIndex() + 1)
            ], self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())] = (
                dict(self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]),
                dict(self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex() + 1)]),
            )

            self.tabWidgetModifiersSets.setCurrentIndex(self.tabWidgetModifiersSets.currentIndex() + 1)
            self.tabMem = self.tabWidgetModifiersSets.currentIndex()


    def moveModifierUp(self):
        """
        move up the selected modifier
        """
        if self.lwModifiers.currentRow() >= 0:
            currentRow = self.lwModifiers.currentRow()
            currentItem = self.lwModifiers.takeItem(currentRow)
            self.lwModifiers.insertItem(currentRow - 1, currentItem)
            self.lwModifiers.setCurrentItem(currentItem)
            self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]["values"] = [self.lwModifiers.item(x).text()
                                                                                                   for x in range(self.lwModifiers.count())]


    def moveModifierDown(self):
        """
        move down the selected modifier
        """
        if self.lwModifiers.currentRow() >= 0:
            currentRow = self.lwModifiers.currentRow()
            currentItem = self.lwModifiers.takeItem(currentRow)
            self.lwModifiers.insertItem(currentRow + 1, currentItem)
            self.lwModifiers.setCurrentItem(currentItem)
            self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]["values"] = [self.lwModifiers.item(x).text()
                                                                                                   for x in range(self.lwModifiers.count())]


    def addSet(self):
        """
        Add a set of modifiers
        """

        # no modifiers set
        if self.tabWidgetModifiersSets.currentIndex() == -1:
            self.modifiers_sets_dict[str(len(self.modifiers_sets_dict))] = {"name": "", "type": SINGLE_SELECTION, "values": []}
            self.tabWidgetModifiersSets.addTab(QWidget(), f"Set #{len(self.modifiers_sets_dict)}")
            self.tabWidgetModifiersSets.setCurrentIndex(self.tabWidgetModifiersSets.count() - 1)
            self.tabMem = self.tabWidgetModifiersSets.currentIndex()

            # set visible and available buttons and others elements
            for w in [self.lbSetName, self.lbType, self.lbValues, self.leSetName, self.cbType, self.lwModifiers, self.pbMoveUp,
                      self.pbMoveDown, self.pbRemoveModifier, self.pbRemoveSet, self.pbMoveSetLeft, self.pbMoveSetRight]:
                w.setVisible(True)
            for w in [self.leModifier, self.leCode, self.pbAddModifier, self.pbModifyModifier]:
                w.setEnabled(True)
            return

        if len(self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]):
            self.modifiers_sets_dict[str(len(self.modifiers_sets_dict))] = {"name": "", "type": SINGLE_SELECTION, "values": []}
            self.tabWidgetModifiersSets.addTab(QWidget(), f"Set #{len(self.modifiers_sets_dict)}")
            self.tabWidgetModifiersSets.setCurrentIndex(self.tabWidgetModifiersSets.count() - 1)
            self.tabMem = self.tabWidgetModifiersSets.currentIndex()

        else:
            QMessageBox.information(self, programName,
                                    "It is not possible to add a modifiers' set while the current modifiers' set is empty.")


    def removeSet(self):
        """
        remove set of modifiers
        """

        if self.tabWidgetModifiersSets.currentIndex() != -1:
            if dialog.MessageDialog(programName, "Confirm deletion of this set of modifiers?", [YES, NO]) == YES:
                index_to_delete = self.tabWidgetModifiersSets.currentIndex()

                for k in range(index_to_delete, len(self.modifiers_sets_dict) - 1):
                    self.modifiers_sets_dict[str(k)] = self.modifiers_sets_dict[str(k + 1)]
                # del last key
                del self.modifiers_sets_dict[str(len(self.modifiers_sets_dict) - 1)]

                # remove all tabs
                while self.tabWidgetModifiersSets.count():
                    self.tabWidgetModifiersSets.removeTab(0)

                # recreate tabs
                for idx in sorted_keys(self.modifiers_sets_dict):
                    self.tabWidgetModifiersSets.addTab(QWidget(), f"Set #{int(idx) + 1}")

                # set not visible and not available buttons and others elements
                if self.tabWidgetModifiersSets.currentIndex() == -1:
                    for w in [self.lbSetName, self.lbType, self.lbValues, self.leSetName, self.cbType, self.lwModifiers, self.pbMoveUp,
                              self.pbMoveDown, self.pbRemoveModifier, self.pbRemoveSet, self.pbMoveSetLeft, self.pbMoveSetRight]:
                        w.setVisible(False)
                    for w in [self.leModifier, self.leCode, self.pbAddModifier, self.pbModifyModifier]:
                        w.setEnabled(False)
        else:
            QMessageBox.information(self, programName, "It is not possible to remove the last modifiers' set.")


    def modifyModifier(self):
        """
        modify modifier <- arrow
        """

        if self.lwModifiers.currentRow() >= 0:
            txt = self.lwModifiers.currentItem().text()
            code = ""
            if "(" in txt and ")" in txt:
                code = txt.split("(")[1].split(")")[0]

            self.leModifier.setText(txt.split("(")[0].strip())
            self.leCode.setText(code)

            self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())][
                "values"
            ].remove(self.lwModifiers.currentItem().text())

            self.itemPositionMem = self.lwModifiers.currentRow()
            self.lwModifiers.takeItem(self.lwModifiers.currentRow())
        else:
            QMessageBox.information(self, programName, "Select a modifier to modify from the modifiers set")


    def removeModifier(self):
        """
        remove modifier from set
        """
        if self.lwModifiers.currentIndex().row() >= 0:
            self.lwModifiers.takeItem(self.lwModifiers.currentIndex().row())
            self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]["values"] = [self.lwModifiers.item(x).text()
                                                                                                   for x in range(self.lwModifiers.count())]


    def addModifier(self):
        """
        add a modifier to set
        """

        txt = self.leModifier.text().strip()
        for c in CHAR_FORBIDDEN_IN_MODIFIERS:
            if c in txt:
                QMessageBox.critical(self, programName,
                                     (f"The character <b>{c}</b> is not allowed.<br>"
                                      "The following characters are not allowed in modifiers:<br>"
                                      f"<b>{CHAR_FORBIDDEN_IN_MODIFIERS}</b>"))
                self.leModifier.setFocus()
                return

        if txt:
            if not self.modifiers_sets_dict:
                self.modifiers_sets_dict["0"] = {"name": "", "type": SINGLE_SELECTION, "values": []}

            if len(self.leCode.text().strip()) > 1:
                if self.leCode.text().strip().upper() not in function_keys.values():
                    QMessageBox.critical(self, programName,
                                         "The modifier key code can not exceed one key\nSelect one key or a function key (F1, F2 ... F12)")
                    self.leCode.setFocus()
                    return

            if self.leCode.text().strip():
                for c in CHAR_FORBIDDEN_IN_MODIFIERS:
                    if c in self.leCode.text().strip():
                        QMessageBox.critical(self, programName,
                                             f"The modifier key code is not allowed {CHAR_FORBIDDEN_IN_MODIFIERS}!")
                        self.leCode.setFocus()
                        return

                # check if code already exists
                if not self.modifiers_sets_dict:
                    self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())] = {"name": "",
                                                                                                 "type": SINGLE_SELECTION,
                                                                                                 "values": []}

                if "(" + self.leCode.text().strip() + ")" in " ".join(
                    self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]["values"]
                ):

                    QMessageBox.critical(self, programName,
                                         f"The shortcut code <b>{self.leCode.text().strip()}</b> already exists!")
                    self.leCode.setFocus()
                    return
                txt += f" ({self.leCode.text().strip()})"

            if self.itemPositionMem != -1:
                self.lwModifiers.insertItem(self.itemPositionMem, txt)
            else:
                self.lwModifiers.addItem(txt)

            self.modifiers_sets_dict[str(self.tabWidgetModifiersSets.currentIndex())]["values"] = [self.lwModifiers.item(x).text()
                                                                                                   for x in range(self.lwModifiers.count())]
            self.leModifier.setText("")
            self.leCode.setText("")

        else:
            QMessageBox.critical(self, programName, "No modifier to add!")
            self.leModifier.setFocus()


    def tabWidgetModifiersSets_changed(self, tabIndex):
        """
        user changed the tab widget
        """

        # check if modifier field empty
        if self.leModifier.text() and tabIndex != self.tabMem:
            if dialog.MessageDialog(programName, ("You are working on a behavior.<br>"
                                                  "If you change the modifier's set it will be lost.<br>"
                                                  "Do you want to change modifiers set"), [YES, NO]) == NO:
                self.tabWidgetModifiersSets.setCurrentIndex(self.tabMem)
                return

        if tabIndex != self.tabMem:
            self.lwModifiers.clear()
            self.leCode.clear()
            self.leModifier.clear()

            self.tabMem = tabIndex

            if tabIndex != -1:
                self.leSetName.setText(self.modifiers_sets_dict[str(tabIndex)]["name"])
                self.cbType.setCurrentIndex(self.modifiers_sets_dict[str(tabIndex)]["type"])
                self.lwModifiers.addItems(self.modifiers_sets_dict[str(tabIndex)]["values"])


    def getModifiers(self):
        """
        returns modifiers as string
        """
        keys_to_delete = []
        for idx in self.modifiers_sets_dict:
            if self.modifiers_sets_dict[idx]["type"] in [SINGLE_SELECTION, MULTI_SELECTION] and not self.modifiers_sets_dict[idx]["values"]:
                keys_to_delete.append(idx)

        for idx in keys_to_delete:
            del self.modifiers_sets_dict[idx]

        return str(self.modifiers_sets_dict) if self.modifiers_sets_dict else ""
