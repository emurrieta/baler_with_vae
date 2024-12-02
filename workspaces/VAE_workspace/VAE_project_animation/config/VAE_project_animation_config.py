
# === Configuration options ===

def set_config(c):
    c.input_path                   = "workspaces/VAE_workspace/data/VAE_project_animation_data.npz"
    c.data_dimension               = 2
    c.compression_ratio            = 4.0
    c.apply_normalization          = False
    c.model_name                   = "VAE"
    c.model_type                    = "dense"
    c.epochs                       = 2000
    c.lr                           = 0.0001
    c.batch_size                   = 60
    c.early_stopping               = False
    c.lr_scheduler                 = True
    c.save_error_bounded_deltas    = False
    c.convert_to_blocks            = False
    c.custom_loss_function         = "loss_function_for_vae"


# === Additional configuration options ===

    c.early_stopping_patience      = 100
    c.min_delta                    = 0
    c.lr_scheduler_patience        = 50
    c.custom_norm                  = False
    c.reg_param                    = 0.001
    c.RHO                          = 0.05
    c.test_size                    = 0
    # c.number_of_columns            = 24
    # c.latent_space_size            = 12
    c.extra_compression            = False
    c.intermittent_model_saving    = False
    c.intermittent_saving_patience = 100
    c.mse_avg                      = False
    c.mse_sum                      = True
    c.emd                          = False
    c.l1                           = True
    c.activation_extraction        = False
    c.deterministic_algorithm      = False
    c.separate_model_saving        = False

