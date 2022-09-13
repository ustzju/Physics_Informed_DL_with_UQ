from utility import set_directory, set_gui_len
from utility import create_paths
from postprocessing import Storage, Plotter
import os

set_directory()
gui_len = set_gui_len()

def print_selection(base_folder, message):
    print(" SELECTION ".center(gui_len,'*'))
    print(f"Available {message}s:")
    for code, folder in enumerate(os.listdir(base_folder)[1:]):
        print(f"{code+1:2d}) {folder}")

def choose_folder(base_folder, message):
    print_selection(base_folder, message)
    code = int(input(f"Select code of chosen {message}: "))
    return os.listdir(base_folder)[code]

base_path = "../outs"
prob_name = choose_folder(base_path, "problem")
prob_path = os.path.join("../outs", prob_name)
case_name = choose_folder(prob_path, "setup case")
case_path = os.path.join(prob_path, case_name)
test_name = choose_folder(case_path, "test case")
test_path = os.path.join(case_path, test_name)

print(" START ".center(gui_len,'*'))
print("Loading data...")
plotter = Plotter(os.path.join(test_path,"plot"))
load_storage = Storage(test_path)
print("Plotting the history...")
plotter.plot_losses(load_storage.history)
#plotter.plot_sigmas(load_storage.sigmas)
print("Plotting the results...")
loaded_data  = load_storage.data
plotter.plot_confidence(loaded_data[0], loaded_data[1], load_storage.confidence)
plotter.plot_nn_samples(loaded_data[0], loaded_data[1], load_storage.nn_samples)
print(" END ".center(gui_len,'*'))

plotter.show_plot()