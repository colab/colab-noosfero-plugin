colab_apps = {
    'colab_noosfero': {
        'menu_title': None,
        'private_token': 'token',
        'upstream': 'localhost',
        'urls': {
            'include': 'colab_noosfero.urls',
            'namespace': 'social',
            'prefix': 'social/'
        }
    }
}

community_json = {
   "communities":[
      {
         "identifier":"software_test_community",
         "name":"Software Test Community",
         "id":71,
         "created_at":"2015/10/06 17:43:45",
         "updated_at":"2015/10/06 17:49:51",
         "image":None,
         "region":None,
         "description":None,
         "admins":[
            {
               "name":"admin admin",
               "username":"admin_admin",
               "id":68
            }
         ],
         "categories":[
         ],
         "members":[
            {
               "identifier":"admin",
               "name":"admin admin",
               "id":68,
               "created_at":"2015/09/29 14:23:09",
               "updated_at":"2015/09/29 14:23:12",
               "image":None,
               "region":None,
               "user":{
                  "id":53,
                  "login":"admin"
               }
            }
         ]
      },
      {
         "identifier":"software_test_community_2",
         "name":"software TEST community 2",
         "id":69,
         "created_at":"2015/09/29 14:36:58",
         "updated_at":"2015/10/28 13:34:41",
         "image":{
            "url":"/image_uploads/0000/0001/gravatar_1.jpg",
            "icon_url":"/image_uploads/0000/0001/gravatar_1_icon.jpg",
            "minor_url":"/image_uploads/0000/0001/gravatar_1_minor.jpg",
            "portrait_url":"/image_uploads/0000/0001/gravatar_1_portrait.jpg",
            "thumb_url":"/image_uploads/0000/0001/gravatar_1_thumb.jpg"
         },
         "region":None,
         "description":None,
         "admins":[
            {
               "name":"user admin",
               "username":"admin_admin",
               "id":69
            }
         ],
         "categories":[
         ],
         "members":[
            {
               "identifier":"user",
               "name":"user admin",
               "id":69,
               "created_at":"2015/09/29 14:23:09",
               "updated_at":"2015/09/29 14:23:12",
               "image":None,
               "region":None,
               "user":{
                  "id":54,
                  "login":"user"
               }
            }
         ]
      }
   ]
}

articles_json  = {
   "articles":[
      {
         "id":211,
         "body":None,
         "abstract":None,
         "created_at":"2015/10/06 17:43:46",
         "updated_at":"2015/10/06 17:43:46",
         "title":"Gallery",
         "author":None,
         "profile":{
            "identifier":"software_test_community",
            "name":"Software Test Community",
            "id":71,
            "created_at":"2015/10/06 17:43:45",
            "updated_at":"2015/10/06 17:49:51",
            "image":None,
            "region":None
         },
         "categories":[
         ],
         "image":None,
         "votes_for":0,
         "votes_against":0,
         "setting":{
         },
         "position":None,
         "hits":0,
         "start_date":None,
         "end_date":None,
         "tag_list":[
         ],
         "children_count":0,
         "slug":"gallery",
         "path":"gallery",
         "parent":None,
         "children":[
         ]
      },
      {
         "id":210,
         "body":{
         },
         "abstract":None,
         "created_at":"2015/10/06 17:43:45",
         "updated_at":"2015/10/06 17:43:45",
         "title":"feed",
         "author":None,
         "profile":{
            "identifier":"software_test_community",
            "name":"Software Test Community",
            "id":71,
            "created_at":"2015/10/06 17:43:45",
            "updated_at":"2015/10/06 17:49:51",
            "image":None,
            "region":None
         },
         "categories":[
         ],
         "image":None,
         "votes_for":0,
         "votes_against":0,
         "setting":{
         },
         "position":None,
         "hits":0,
         "start_date":None,
         "end_date":None,
         "tag_list":[
         ],
         "children_count":0,
         "slug":"feed",
         "path":"blog/feed",
         "parent":{
            "id":209,
            "body":None,
            "abstract":None,
            "created_at":"2015/10/06 17:43:45",
            "updated_at":"2015/10/06 17:43:45",
            "title":"Blog",
            "author":None,
            "profile":{
               "identifier":"software_test_community",
               "name":"Software Test Community",
               "id":71,
               "created_at":"2015/10/06 17:43:45",
               "updated_at":"2015/10/06 17:49:51",
               "image":None,
               "region":None
            },
            "categories":[
            ],
            "image":None,
            "votes_for":0,
            "votes_against":0,
            "setting":{
            },
            "position":None,
            "hits":0,
            "start_date":None,
            "end_date":None,
            "tag_list":[
            ],
            "children_count":1,
            "slug":"blog",
            "path":"blog"
         },
         "children":[
         ]
      },
      {
         "id":209,
         "body":None,
         "abstract":None,
         "created_at":"2015/10/06 17:43:45",
         "updated_at":"2015/10/06 17:43:45",
         "title":"Blog",
         "author":None,
         "profile":{
            "identifier":"software_test_community",
            "name":"Software Test Community",
            "id":71,
            "created_at":"2015/10/06 17:43:45",
            "updated_at":"2015/10/06 17:49:51",
            "image":None,
            "region":None
         },
         "categories":[
         ],
         "image":None,
         "votes_for":0,
         "votes_against":0,
         "setting":{
         },
         "position":None,
         "hits":0,
         "start_date":None,
         "end_date":None,
         "tag_list":[
         ],
         "children_count":1,
         "slug":"blog",
         "path":"blog",
         "parent":None,
         "children":[
            {
               "id":210,
               "body":{
               },
               "abstract":None,
               "created_at":"2015/10/06 17:43:45",
               "updated_at":"2015/10/06 17:43:45",
               "title":"feed",
               "author":None,
               "profile":{
                  "identifier":"software_test_community",
                  "name":"Software Test Community",
                  "id":71,
                  "created_at":"2015/10/06 17:43:45",
                  "updated_at":"2015/10/06 17:49:51",
                  "image":None,
                  "region":None
               },
               "categories":[
               ],
               "image":None,
               "votes_for":0,
               "votes_against":0,
               "setting":{
               },
               "position":None,
               "hits":0,
               "start_date":None,
               "end_date":None,
               "tag_list":[
               ],
               "children_count":0,
               "slug":"feed",
               "path":"blog/feed"
            }
         ]
      }
   ]
}
