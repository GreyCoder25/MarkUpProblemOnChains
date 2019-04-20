import numpy as np


class TObject(object):
    def __init__(self, index, labels, neighbors_indexes, q_init=np.inf):
        self.index = index
        self.neighbors_back = []
        self.num_labels = len(labels)
        self.labels = labels
        self.q = {label: q_init for label in labels}
        self.prev_label = {label: None for label in labels}
        self.prev_object = {label: None for label in labels}
        self._set_neighbors(neighbors_indexes)
        self._initialize_edges(np.inf)

    def _initialize_edges(self, init_value):
        self.g = {neighbor_index: {label: dict() for label in self.labels} for neighbor_index in self.neighbors_back}
        if self.neighbors_back:
            for t_ in self.neighbors_back:
                for k_ in self.labels:
                    for k in self.labels:
                        self.g[t_][k_][k] = init_value
        # else:
        #     print('NEIGHBORS ARE NOT DEFINED FOR OBJECT {}'.format(self.index))

    def _set_neighbors(self, neighbors_relative_indexes):
        for neighbor_relative_index in neighbors_relative_indexes:
            if self.index - neighbor_relative_index >= 0:
                self.neighbors_back.append(self.index - neighbor_relative_index)


def general_mark_up(objects):
    for obj_index, obj in enumerate(objects):
        for neighbor_index in obj.neighbors_back:
            for k in obj.labels:
                min_q = np.inf
                for k_ in obj.labels:
                    subpath_len = objects[neighbor_index].q[k_] + obj.g[neighbor_index][k_][k]
                    if subpath_len < min_q:
                        min_q = subpath_len
                        obj.q[k] = subpath_len
                        obj.prev_label[k] = k_
                        obj.prev_object[k] = neighbor_index

    best_path_len = np.inf
    last_label = None
    for label in objects[-1].q:
        if objects[-1].q[label] < best_path_len:
            best_path_len = objects[-1].q[label]
            last_label = label

    labeling = ''
    obj_index = -1
    label = last_label
    while label is not None:
        labeling = label + labeling
        next_label = label
        label = objects[obj_index].prev_label[label]
        obj_index = objects[obj_index].prev_object[next_label]
        if obj_index == 0:
            break
    return labeling


if __name__ == '__main__':
    NUM_OBJECTS = 20
    LABELS = ['A', 'B', 'C', '_']
    NEIGHBORS_RELATIVE_INDEXES = [1, 5, 8, 10]
    objects = [TObject(i, LABELS, NEIGHBORS_RELATIVE_INDEXES) for i in range(NUM_OBJECTS)]

