from pathlib import Path
import trimesh
def glb_to_obj(glb_path):
    # Load the .glb file
    mesh = trimesh.load(glb_path, force='scene')
    
    # Generate the corresponding .obj file path
    obj_path = glb_path.with_suffix('.obj')
    
    # Export the mesh to the .obj format
    mesh.export(obj_path)
    print(f"Converted {glb_path} to {obj_path}")

def convert_glb_to_obj_in_directory(meshes_dir_path):
    # Convert the directory path to a Path object
    meshes_dir = Path(meshes_dir_path)
    
    # Find all .glb files in the directory
    glb_meshes_paths = [p for p in meshes_dir.glob("*.glb")]
    
    # Convert each .glb file to .obj
    for glb_path in glb_meshes_paths:
        glb_to_obj(glb_path)

# Example usage:
meshes_dir_path = Path(__file__).parent / "meshes" / "visual"
convert_glb_to_obj_in_directory(meshes_dir_path)
