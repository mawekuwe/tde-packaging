/*
    This file is part of KitchenSync.

    Copyright (c) 2005 Cornelius Schumacher <schumacher@kde.org>
    Copyright (c) 2008 Eduardo Habkost <ehabkost@raisama.net>
    Copyright (c) 2008 Adam Williamson <awilliamson@mandriva.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
    USA.
*/

#include "configguibarry.h"

#include <klocale.h>

#include <qlayout.h>
#include <qlabel.h>
#include <qdom.h>
#include <qlineedit.h>
#include <qcheckbox.h>

ConfigGuiBarry::ConfigGuiBarry( const QSync::Member &member, QWidget *parent )
  : ConfigGui( member, parent )
{
  QBoxLayout *userLayout = new QHBoxLayout( topLayout() );

  QLabel *pinLbl= new QLabel( i18n("PIN:"), this );
  userLayout->addWidget(pinLbl);

  mPin = new QLineEdit(this);
  userLayout->addWidget(mPin);

  mCalendar = new QCheckBox( i18n("Sync calendar"), this );
  userLayout->addWidget( mCalendar );

  mContacts = new QCheckBox( i18n("Sync contacts"), this );
  userLayout->addWidget( mContacts );

  topLayout()->addStretch( 1 );
}

void ConfigGuiBarry::load(const QString &cfg)
{
        QStringList lines = QStringList::split( '\n', cfg);
	QString pin;
	uint cal = 0;
	uint con = 0;
        for ( QStringList::Iterator it = lines.begin(); it != lines.end(); ++it ) {
                QStringList options = QStringList::split( ' ', *it);
		if (options.count() < 1)
			/* invalid line */
			continue;

                if( options[0].lower() == "device" )
                {
			if (options.count() < 2)
            			/* invalid line */
            			continue;

                        pin = options[1];
			if (options.count() >= 3)
                        	cal = options[2].toUInt();
			if (options.count() >= 4)
	                        con = options[3].toUInt();
                        
                        mPin->setText(pin);
			mCalendar->setChecked( cal != 0);
			mContacts->setChecked( con != 0);
                }
        }
}

QString ConfigGuiBarry::save() const
{
  QString cfg;
  cfg = "Device " + mPin->text();
  if ( mCalendar->isChecked() ) cfg += " 1";
  else cfg += " 0";
  if ( mContacts->isChecked() ) cfg += " 1";
  else cfg += " 0";

  return cfg;
}
