package net.helix.pendulum.conf;

/**
 *
 * Configurations that should be used for the tip solidification process,
 * You can also completely disable the process.
 */
public interface SolidificationConfig extends Config {

    /**
     * Default Value: {@value BasePendulumConfig.Defaults#TIP_SOLIDIFIER_ENABLED}
     *
     * @return {@value SolidificationConfig.Descriptions#TIP_SOLIDIFIER}
     */
    boolean isTipSolidifierEnabled();

    /**
     * Default Value: {@value BasePendulumConfig.Defaults#SOLIDIFICATION_QUEUE_CAP}
     * @return {@value SolidificationConfig.Descriptions#SOLIDIFICATION_QUEUE_CAP}
     */
    int getSolidificationQueueCap();

    /**
     * Field descriptions
     */
    interface Descriptions {

        String TIP_SOLIDIFIER = "Scan the current tips and attempt to mark them as solid";
        String SOLIDIFICATION_QUEUE_CAP = "?";
    }
}
