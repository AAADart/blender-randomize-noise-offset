bl_info = {
    "name": "Randomize Noise Offset (Graph Editor)",
    "author": "ChatGPT",
    "version": (1, 0, 1),
    "blender": (4, 0, 0),
    "location": "Graph Editor ▶ N-panel ▶ Modifiers",
    "description": "Randomize the Offset of NOISE F-Curve modifiers for selected objects' actions (offset specified in seconds).",
    "category": "Animation",
}

import bpy
import random
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import IntProperty, FloatProperty, PointerProperty

# -----------------------------------------------------------------------------
# Properties kept on Scene via a PropertyGroup (clean register/unregister)
# -----------------------------------------------------------------------------

class RNO_Props(PropertyGroup):
    seed: IntProperty(
        name="Seed",
        description="Random seed for reproducibility",
        default=12345,
        min=-2**31,
        max=2**31-1,
    )
    offset_min: FloatProperty(
        name="Offset Min (s)",
        description="Minimum offset in seconds",
        default=0.0,
        soft_min=0.0,
    )
    offset_max: FloatProperty(
        name="Offset Max (s)",
        description="Maximum offset in seconds",
        default=10.0,
        soft_min=0.0,
    )

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def _collect_target_objects(context):
    objs = [o for o in (context.selected_objects or []) if getattr(o.animation_data, "action", None)]
    if not objs and context.active_object and getattr(context.active_object.animation_data, "action", None):
        objs = [context.active_object]
    return objs

# -----------------------------------------------------------------------------
# Operator
# -----------------------------------------------------------------------------

class GRAPH_OT_randomize_noise_offset(Operator):
    bl_idname = "graph.randomize_noise_offset"
    bl_label = "Randomize Noise Offset"
    bl_description = "Assign a random Offset (in seconds) to every NOISE modifier on F-Curves of selected objects' active actions"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        props = context.scene.rno_props
        seed = int(props.seed)
        off_min = float(props.offset_min)
        off_max = float(props.offset_max)

        if off_max < off_min:
            off_min, off_max = off_max, off_min

        fps = context.scene.render.fps / max(1.0, context.scene.render.fps_base)
        random.seed(seed)

        objs = _collect_target_objects(context)
        if not objs:
            self.report({'WARNING'}, "Немає об'єктів з активною дією (Action). Оберіть об'єкти або активний об'єкт із анімацією.")
            return {'CANCELLED'}

        count = 0
        for ob in objs:
            act = ob.animation_data.action
            if not act:
                continue
            for fc in act.fcurves:
                for mod in fc.modifiers:
                    if mod.type == 'NOISE':
                        mod.offset = random.uniform(off_min, off_max) * fps
                        count += 1

        self.report({'INFO'}, f"✅ Оновлено {count} Noise-модифікатор(ів) на {len(objs)} об'єкт(ах).")
        return {'FINISHED'}

# -----------------------------------------------------------------------------
# UI Panel (Graph Editor ▶ N ▶ Modifiers)
# -----------------------------------------------------------------------------

class GRAPH_PT_randomize_noise_offset(Panel):
    bl_space_type = 'GRAPH_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Modifiers'  # помістити в існуючу вкладку Graph Editor
    bl_label = 'Randomize Noise Offset'  # з'явиться у вкладці Modifiers

    def draw(self, context):
        layout = self.layout
        props = context.scene.rno_props

        col = layout.column(align=True)
        col.prop(props, "seed")
        col.prop(props, "offset_min")
        col.prop(props, "offset_max")
        col.operator(GRAPH_OT_randomize_noise_offset.bl_idname, icon='MOD_NOISE')

# -----------------------------------------------------------------------------
# Registration
# -----------------------------------------------------------------------------

classes = (
    RNO_Props,
    GRAPH_OT_randomize_noise_offset,
    GRAPH_PT_randomize_noise_offset,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.rno_props = PointerProperty(type=RNO_Props)


def unregister():
    del bpy.types.Scene.rno_props
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
