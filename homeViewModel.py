import os
from PIL import Image
from event import post_event, post_event_async

class HomeViewModel:
    def __init__(self, rotate_image_use_case, translation_image_use_case, scale_image_use_case):
        self.rotate_image_use_case = rotate_image_use_case 
        self.translation_image_use_case = translation_image_use_case 
        self.scale_image_use_case = scale_image_use_case
        self.image_modified = None
        self.image_path = ""
        self.location_save_image = ""
        self.input_from_dialog = ""
    
    async def update_path(self, value):
        self.image_path = value
    
    async def update_location_save_image(self, value):
        self.location_save_image = value
    
    async def update_input_from_dialog(self, value):
        self.input_from_dialog = value
    
    async def save_image_on_locatin(self):
        #image = ImageTk.getimage(self.image_modify._get_scaled_light_photo_image(scaled_size=(self.weight, self.height)))
        #image.save(os.path.join(location))
        self.image_modified.save(os.path.join(self.location_save_image))
    
    async def first_load_image_on_labels(self):
        self.image_modified = Image.open(os.path.join(self.image_path))
        post_event("update_image_transformed_label", self.image_modified)
        post_event("update_image_original_label", self.image_modified)
    
    async def rotate_image(self):
        await post_event_async("get_input_from_dialog")
        self.image_modified = await self.rotate_image_use_case.execute(self.image_modified, float(self.input_from_dialog))
        post_event("update_image_transformed_label", self.image_modified)
    
    async def translation_image(self): 
        await post_event_async("get_input_from_dialog")
        self.image_modified = self.translation_image_use_case.execute(self.image_modified, float(self.input_from_dialoge))
        post_event("update_image_transformed_label", self.image_modified)
    
    async def scale_image(self):
        await post_event_async("get_input_from_dialog")
        self.image_modified = self.scale_image_use_case.execute(self.image_modified, float(self.input_from_dialog))
        post_event("update_image_transformed_label", self.image_modified)
        