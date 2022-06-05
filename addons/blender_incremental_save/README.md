# Blender Incremental Save

**Incremental Save** gives you the ability of quick and simple create the new version of your file based on its naming.
It splits the file name by digits and letters parts and adds the necessary number to the last digits part so that your new file name won't overwrite the other versions.

After being installed this add-on ads the **Incremental Save** operator to the top of the File Menu.
You can click it there or add the shortcut.
![image](https://user-images.githubusercontent.com/59086089/172042842-cda8d2d9-8c49-4eb4-8659-e8f884e83043.png)


## Examples of the Incremental Save naming convention:
- file is not saved -> **file is saved under the deisired name in a desired folder**
- untitled.blend -> **untitled1.blend** (if you don't have numvers at all then the add-on will add 1 (or any bigger number for not matching the exisiting ones) just to start with something)
- scene1.blend -> **scene2.blend**
- scene000.blend -> **scene001.blend**
- file_v09.blend -> **file_v10.blend**
- file0099.blend -> **file0100.blend**
- Sc01_shot025_final.blend - > **Sc01_shot026_final.blend**
