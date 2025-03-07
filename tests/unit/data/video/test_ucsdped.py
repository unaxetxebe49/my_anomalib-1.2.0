"""Unit Tests - UCSDped Datamodule."""

# Copyright (C) 2023-2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

import pytest

from anomalib import TaskType
from anomalib.data import UCSDped
from tests.unit.data.base.video import _TestAnomalibVideoDatamodule


class TestUCSDped(_TestAnomalibVideoDatamodule):
    """UCSDped Datamodule Unit Tests."""

    @pytest.fixture()
    @staticmethod
    def clip_length_in_frames() -> int:
        """Return the number of frames in each clip."""
        return 2

    @pytest.fixture()
    @staticmethod
    def datamodule(dataset_path: Path, task_type: TaskType, clip_length_in_frames: int) -> UCSDped:
        """Create and return a UCSDped datamodule."""
        _datamodule = UCSDped(
            root=dataset_path / "ucsdped",
            category="dummy",
            clip_length_in_frames=clip_length_in_frames,
            task=task_type,
            image_size=256,
            train_batch_size=4,
            eval_batch_size=4,
            num_workers=0,
        )
        _datamodule.prepare_data()
        _datamodule.setup()

        return _datamodule

    @pytest.fixture()
    @staticmethod
    def fxt_data_config_path() -> str:
        """Return the path to the test data config."""
        return "configs/data/ucsd_ped.yaml"
