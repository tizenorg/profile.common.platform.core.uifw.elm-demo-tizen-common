/*
 * Copyright (c) 2015 Samsung Electronics Co., Ltd All Rights Reserved
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 */

#include "main.h"
#include <app_control.h>

static void
list_selected_cb(void *data, Evas_Object *obj, void *event_info)
{
	Elm_Object_Item *it = event_info;
	elm_list_item_selected_set(it, EINA_FALSE);
}

void
accessibility_cb(void *data, Evas_Object *obj, void *event_info)
{
			app_control_h service;
			int launch_ret;

			if (!app_control_create(&service)) {
				//app_control_set_operation(service, APP_CONTROL_OPERATION_DEFAULT);
				app_control_set_operation(service, APP_CONTROL_OPERATION_PICK);
				app_control_set_app_id(service, "ug-bluetooth-efl");

				app_control_add_extra_data(service, "launch-type", "setting");

				launch_ret = app_control_send_launch_request(service, NULL, NULL);

				app_control_destroy(service);
			}

#if 0
	Evas_Object *list;
	Evas_Object *nf = data;

	/* List */
	list = elm_list_add(nf);
	elm_list_mode_set(list, ELM_LIST_COMPRESS);
	evas_object_smart_callback_add(list, "selected", list_selected_cb, NULL);

	elm_list_item_append(list, "Screen Reader", NULL, NULL, screen_reader_cb, nf);
	elm_list_go(list);

	elm_naviframe_item_push(nf, "Accessibility", NULL, NULL, list, NULL);
#endif
}
