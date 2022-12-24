from enum import Enum

class HandJoint(Enum):
    # PALM
    PALM_EXT = 0
    WRIST_EXT = 1
    # THUMB
    THUMB_METACARPAL_EXT = 2
    THUMB_PROXIMAL_EXT = 3
    THUMB_DISTAL_EXT = 4
    THUMB_TIP_EXT = 5
    # INDEX
    INDEX_METACARPAL_EXT = 6
    INDEX_PROXIMAL_EXT = 7
    INDEX_INTERMEDIATE_EXT = 8
    INDEX_DISTAL_EXT = 9
    INDEX_TIP_EXT = 10
    # MIDDLE
    MIDDLE_METACARPAL_EXT = 11
    MIDDLE_PROXIMAL_EXT = 12
    MIDDLE_INTERMEDIATE_EXT = 13
    MIDDLE_DISTAL_EXT = 14
    MIDDLE_TIP_EXT = 15
    # RING
    RING_METACARPAL_EXT = 16
    RING_PROXIMAL_EXT = 17
    RING_INTERMEDIATE_EXT = 18
    RING_DISTAL_EXT = 19
    RING_TIP_EXT = 20
    # LITTLE
    LITTLE_METACARPAL_EXT = 21
    LITTLE_PROXIMAL_EXT = 22
    LITTLE_INTERMEDIATE_EXT = 23
    LITTLE_DISTAL_EXT = 24
    LITTLE_TIP_EXT = 25
    MAX_ENUM_EXT = 0x7FFFFFFF

hand_bone_map = [
    # PALM
    (HandJoint.WRIST_EXT, HandJoint.PALM_EXT),
    # THUMB
    (HandJoint.WRIST_EXT, HandJoint.THUMB_METACARPAL_EXT),
    (HandJoint.THUMB_METACARPAL_EXT, HandJoint.THUMB_PROXIMAL_EXT),
    (HandJoint.THUMB_PROXIMAL_EXT, HandJoint.THUMB_DISTAL_EXT),
    (HandJoint.THUMB_DISTAL_EXT, HandJoint.THUMB_TIP_EXT),
    # INDEX
    (HandJoint.WRIST_EXT, HandJoint.INDEX_METACARPAL_EXT),
    (HandJoint.INDEX_METACARPAL_EXT, HandJoint.INDEX_PROXIMAL_EXT),
    (HandJoint.INDEX_PROXIMAL_EXT, HandJoint.INDEX_INTERMEDIATE_EXT),
    (HandJoint.INDEX_INTERMEDIATE_EXT, HandJoint.INDEX_DISTAL_EXT),
    (HandJoint.INDEX_DISTAL_EXT, HandJoint.INDEX_TIP_EXT),
    # MIDDLE
    (HandJoint.WRIST_EXT, HandJoint.MIDDLE_METACARPAL_EXT),
    (HandJoint.MIDDLE_METACARPAL_EXT, HandJoint.MIDDLE_PROXIMAL_EXT),
    (HandJoint.MIDDLE_PROXIMAL_EXT,  HandJoint.MIDDLE_INTERMEDIATE_EXT),
    (HandJoint.MIDDLE_INTERMEDIATE_EXT, HandJoint.MIDDLE_DISTAL_EXT),
    (HandJoint.MIDDLE_DISTAL_EXT,  HandJoint.MIDDLE_TIP_EXT),
    # RING
    (HandJoint.WRIST_EXT, HandJoint.RING_METACARPAL_EXT),
    (HandJoint.RING_METACARPAL_EXT, HandJoint.RING_PROXIMAL_EXT),
    (HandJoint.RING_PROXIMAL_EXT, HandJoint.RING_INTERMEDIATE_EXT),
    (HandJoint.RING_INTERMEDIATE_EXT, HandJoint.RING_DISTAL_EXT),
    (HandJoint.RING_DISTAL_EXT, HandJoint.RING_TIP_EXT),
    # LITTLE
    (HandJoint.WRIST_EXT, HandJoint.LITTLE_METACARPAL_EXT),
    (HandJoint.LITTLE_METACARPAL_EXT, HandJoint.LITTLE_PROXIMAL_EXT),
    (HandJoint.LITTLE_PROXIMAL_EXT, HandJoint.LITTLE_INTERMEDIATE_EXT),
    (HandJoint.LITTLE_INTERMEDIATE_EXT, HandJoint.LITTLE_DISTAL_EXT),
    (HandJoint.LITTLE_DISTAL_EXT, HandJoint.LITTLE_TIP_EXT),
]

hand_joint_position = {
    HandJoint.WRIST_EXT : (0,0,0),
    HandJoint.PALM_EXT : (0,0,0),
    HandJoint.THUMB_METACARPAL_EXT : (0,0,0),
    HandJoint.THUMB_PROXIMAL_EXT : (0,0,0),
    HandJoint.THUMB_DISTAL_EXT : (0,0,0),
    HandJoint.THUMB_TIP_EXT : (0,0,0),
    HandJoint.INDEX_METACARPAL_EXT : (0,0,0),
    HandJoint.INDEX_PROXIMAL_EXT : (0,0,0),
    HandJoint.INDEX_INTERMEDIATE_EXT : (1,2,3),
    HandJoint.INDEX_DISTAL_EXT : (1,2,3),
    HandJoint.INDEX_TIP_EXT : (1,2,3),
    HandJoint.MIDDLE_METACARPAL_EXT : (1,2,3),
    HandJoint.MIDDLE_PROXIMAL_EXT : (1,2,3),
    HandJoint.MIDDLE_INTERMEDIATE_EXT : (1,2,3),
    HandJoint.MIDDLE_DISTAL_EXT : (1,2,3),
    HandJoint.MIDDLE_TIP_EXT : (1,2,3),
    HandJoint.RING_METACARPAL_EXT : (1,2,3),
    HandJoint.RING_PROXIMAL_EXT : (1,2,3),
    HandJoint.RING_INTERMEDIATE_EXT : (1,2,3),
    HandJoint.RING_DISTAL_EXT : (1,2,3),
    HandJoint.RING_TIP_EXT : (1,2,3),
    HandJoint.LITTLE_METACARPAL_EXT : (1,2,3),
    HandJoint.LITTLE_PROXIMAL_EXT : (1,2,3),
    HandJoint.LITTLE_INTERMEDIATE_EXT : (1,2,3),
    HandJoint.LITTLE_DISTAL_EXT : (1,2,3),
    HandJoint.LITTLE_TIP_EXT : (1,2,3),
}

import bpy
_armature = None 
_ebs = None


def init():
    _armature = bpy.context.active_object
    _ebs = _armature.data.edit_bones
    
    # 새로운 Armature 생성
    bpy.ops.object.armature_add(radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

    # 우선 Edit 모드로 변경
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)


def create_bone(name, head, tail):
    eb = _ebs.new(name)
    eb.head = head
    eb.tail = tail
    return eb

def link(parent, child):
    parent = _armature.data.edit_bones[parent]
    child = _armature.data.edit_bones[child]
    child.parent = parent
    child.use_connect = True

def create_bones():
    for joint in range(0,len(hand_bone_map)):
        j = hand_bone_map[joint]
        parent = j[0]
        child = j[1]

        parent_pos = hand_joint_position[parent]
        child_pos = hand_joint_position[child]

        print(child.name, parent_pos, child_pos)
        create_bone(child.name, parent_pos, child_pos)
        link(parent.name, child.name)

init()
create_bones()

