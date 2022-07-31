# Stack Visible FCurves

When you work with a really big amount of **Animation Curves** in Blender's **Graph Editor** you may want to hide some of them (which you don't need to inspect currently) in sake of making the Graph Editor workspace more clear and readable.
However the presence of the **FCurve** at the main Sheet doesn't affect the list of the **Groups** in the left panel of the **Graph Editor**. Which means you'll need to scroll this list all the way down searching for the Groups containing those very FCurves you wanted to left visible.

Generally this tiny add-on is inspired by [**this**](https://developer.blender.org/T71238) claim. It doesn't add the whole desired functionality (as we cannot simply *subtract* the Groups from the Graph Editor with Python API) but at least helps you to keep the list of the Groups in a more organized way.

**IMPORTANT!** currently the add-on works only for the **Armature** (*Pose Bones*) animation as it is the most popular case in character animation and often leads you to the way where you have quite a big amount of the FCurves

### Placement
After being installed the add-ons one and only button will be placed in the bottom of the **Graph Editor's Channel** Menu.
![image](https://user-images.githubusercontent.com/59086089/182045652-d8bc42ed-e7ea-4da0-b2af-5f7944f1533e.png)

### Use Case
1. Select the **Keyframe Points** of the Animaton Channels you want to leave **visible** and click on **Channel** -> **Hide Unselected Curves** button.
2. Click on **Channel** -> **Stack Visible** button.
3. This operator will move all the **Groups** that countain **Visible** Fcurves to the **Top** of the list in the **Grapf Editor**.
4. The **FCurves** that are Visible but **not groupped** will be groupped under the **"UNGROUPPED"** label.
5. All the **Groups** that contain the **hidden** FCurves will be **collapsed**.

## Additional Functions
After the **Stack Visible** operator is executed it will have the pop-up menu with two additional functions
![image](https://user-images.githubusercontent.com/59086089/182045943-29834646-ecad-43b9-a6b1-0c48e3f17f2c.png)
1. **Expand**: all the stacked Groups will be Expanded while the others will stay Collapsed
2. **Pin**: all the stacked Groups will be Pinned while the others Unpinned (pinning will let you clear/change the Pose Bones selection and still have the ability to have these stacked Groups placed in the list of the Channels in the Graph Editor)
