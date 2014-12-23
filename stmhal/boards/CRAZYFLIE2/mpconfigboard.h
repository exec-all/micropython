#define CRAZYFLIE2

#define MICROPY_HW_BOARD_NAME       "Crazyflie 2.0 Rev.C"
#define MICROPY_HW_MCU_NAME         "STM32F405RG"
#define MICROPY_PY_SYS_PLATFORM     "crazyflie2"

#define MICROPY_HW_HAS_SWITCH       (0)
#define MICROPY_HW_HAS_SDCARD       (0)
#define MICROPY_HW_HAS_MMA7660      (0)
#define MICROPY_HW_HAS_LIS3DSH      (0)
#define MICROPY_HW_HAS_LCD          (0)
#define MICROPY_HW_ENABLE_RNG       (1)
#define MICROPY_HW_ENABLE_RTC       (1)
#define MICROPY_HW_ENABLE_TIMER     (1)
#define MICROPY_HW_ENABLE_SERVO     (0)
#define MICROPY_HW_ENABLE_DAC       (0)
#define MICROPY_HW_ENABLE_I2C1      (1)
#define MICROPY_HW_ENABLE_SPI1      (0)
#define MICROPY_HW_ENABLE_SPI3      (0)
#define MICROPY_HW_ENABLE_CAN       (0)

// The pyboard has 4 LEDs
#define MICROPY_HW_LED1             (pin_C0) // red (left)
#define MICROPY_HW_LED2             (pin_C1) // green (left)
#define MICROPY_HW_LED3             (pin_C2) // green (right)
#define MICROPY_HW_LED4             (pin_C3) // red (right)
#define MICROPY_HW_LED_OTYPE        (GPIO_MODE_OUTPUT_PP)
#define MICROPY_HW_LED_ON(pin)      (pin->gpio->BSRRH = pin->pin_mask)
#define MICROPY_HW_LED_OFF(pin)     (pin->gpio->BSRRL = pin->pin_mask)
