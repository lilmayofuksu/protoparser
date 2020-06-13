#!/usr/bin/env python
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from proto3parser import parser

content = '''syntax = "proto3";
package service;
option go_package = "bitbucket.org/funplus/sandwichgmt/backend/pkg/gen/service";
import "msg/job_file.proto";
import "google/api/annotations.proto";

message MessageItem {
    string Title = 1;
    string Content = 2;
}

enum PlayerType {
    //normal player
    NORMAL = 0;
    //cheater
    CHEATER = 1;
    //tester
    TESTER = 2;
    //deleted player
    DELETE = 3;
}

//@entry
//@schema
message Player {
    //player id
    uint64 PlayerId = 1;
    string Name = 2;
    // @max =1000
    int32 Level = 3;
    int32 Coins = 4;
    //@fmt=date
    //@desc=Player's birthday
    string Birthday = 5;
    //@required
    PlayerType Type = 6;
    // @title App version history
    repeated string AppVerHistory = 7;
    repeated MessageItem MessageBox = 8;
    message StoreItem {
        uint32 Num = 1;
        //@title 来源
        string From = 2;
    }
    //@ title =Warehouse
    map<uint64, StoreItem> Storage = 9;
    //fmt =email
    string Email = 10;
    //@pattern=^(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]$
    string HomePage = 11;
    enum InnerType {
        TEST = 0;
        //@dd =33
        OK = 1;
    }
}

service JobFileService {
    rpc GDriveFileList (msg.GDriveFileListReq) returns(msg.FileListRep) {
        option (google.api.http) = {
            post: "/api/files/gdrive"
            body: "*"
        };
    }
}
'''

print(parser.parse(content))
print(parser.serialize2json(content))