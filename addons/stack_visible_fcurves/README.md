# Armature Graph Tools
- ### Overview
When you work with a really big amount of **Animation Curves** in Blender's **Graph Editor** you may want to hide some of them (which you don't need to inspect currently) in sake of making the Graph Editor workspace more clear and readable.
However the presence of the **FCurve** at the main Sheet doesn't affect the list of the **Groups** in the left panel of the **Graph Editor**. Which means you'll need to scroll this list all the way down searching for the Groups containing those very FCurves you wanted to left visible.

Generally this add-on was inspired by [**this**](https://developer.blender.org/T71238) claim. It doesn't add the whole desired functionality (as we cannot simply *subtract* the Groups from the Graph Editor with Python API) but at least helps you to keep the list of the Groups in a more organized way.

The second sector of the add-on is dedicated to synchronize the visibility of the **Grpah Editor's FCurves** with the relevant **Armature's Pose Bones** in the Viewport. You can also force it to syncronize the Pose Bones visibility not with the Visible FCurves but with the **Selected** ones (in other words, with those which keys are selected in the Graph Editor).

⚠**IMPORTANT** The add-on works only for the **Armature** (*Pose Bones*) animation as it is the most popular case in character animation and often leads you to the way where you have quite a big amount of the FCurves

- ### Placement
After being installed the add-on will emerge in the **Graph Editor's N-Panel** in the **Armature** tab. This tab will be vivible only when your Active Object is of **Armature** type.

![image](https://user-images.githubusercontent.com/59086089/189810854-7e7d3a5f-2791-475b-a997-0881670dfc45.png)

## Stack Curves
- ### Use Case
1. Select the **Keyframe Points** of the Animaton Channels you want to leave **visible** and press **Alt+H** (or in the Menu: Channel -> Hide Unselected Curves).
2. Click on **Stack Curves** button.
3. This operator will move all the **Groups** that countain **Visible** Fcurves to the **Top** of the list in the **Grapf Editor**.
4. The **FCurves** that are Visible but **not groupped** will be groupped under the **"UNGROUPPED"** label.
5. All the **Groups** that contain the **hidden** FCurves will be **collapsed**.

- ### Additional Functions
The **Stack Visible** operator is executed taking two additional functions (placed on the top of the button) into account:
![image](https://user-images.githubusercontent.com/59086089/189811717-9795e519-d270-4dbc-906a-07a450bb1d7e.png)
  1. **Expand**: all the stacked Groups will be Expanded while the others will stay Collapsed
  2. **Pin**: all the stacked Groups will be Pinned while the others Unpinned (pinning will let you clear/change the Pose Bones selection and still have the ability to have these stacked Groups placed in the list of the Channels in the Graph Editor)
 
## Sync Pose Bones Visibility
- ### Use Case
1. Select the **Keyframe Points** of the Animaton Channels you want to leave **visible** and press **Alt+H** (or in the Menu: Channel -> Hide Unselected Curves).
2. Click on **Sync Visibility** button: that will hide all the Pose Bones which animation is not among the **Visible FCurves** of the Graph Editor, and it will reveal all the Pose Bones which animation is visible in the Graph Editor by revealing its **Layers** and/or muting its "Hide" **Drivers** and/or just unhiding them in the Viewport if they were previously hidden.
3. **OR** after selecting some Keyframe Points instead of hiding the other FCurves you can just click on **Sync with Selected Curves**: it will make those and only those Pose Bones visible which FCurves (Keyframe Points) are selected.
4. After dealing with Visibility Syncronization if you would like to go to the initial Armature state (by "initial" the Add-On understands the state of Pose Bones and Armature Layers visibility as well as "Hide" Drivers muting that was present at the moment before you click on "Sync Visibility"/"Sync with Selected Curves"). In that case you will need a **Restore Visibility** button.
- ### Additional Functions
1. **Drivers**: whether to override or not the existing Drivers that define the Pose Bone visibility. If turned on (it is by the Default) then all the Drivers that hide/unhide Pose Bones will be mute until the initial Armature state is restored.
2. **Layers**: same here, whether to affect Armature Layers or not. If turned on then Pose Bones at the hidden Armature Layers will become visible by making such Layers visible.
3. **Freeze Layers**: exclude some certain Armature Layers from any Add-On's affection. In other words, Pose Bones at these layers won't be touched no matter should they stay hidden or be revealed.
4. **Freeze Bones Names**: exclude Bones that contain the given string in its name from any Add-On's affection. You can use **\*** symbol for a wildcards search (e.g. *\*chest* will exclude both *hest*and *CTRL-Chest* controllers from the Add-On's job, **spine* will exclude *Spine1*, *Spine2*, *CTRL-Spine* and so on). You can also turn on the Case Sensitive search.
