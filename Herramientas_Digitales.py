{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOlUSlXtTrE8Sht5IyrEwuO",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/fvergara24/2pi/blob/main/Herramientas_Digitales.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install streamlit"
      ],
      "metadata": {
        "id": "jstPWTCy9scs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6Ez9QpPB9UOV",
        "outputId": "79a40cd4-90e6-4924-bc85-53e6d4071bdb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app.py\n",
        "\n",
        "import streamlit as st\n",
        "\n",
        "st.set_page_config(page_title='Equipo 5 - Henry')\n",
        "st.title('Proyecto Grupal - Equipo 5')\n",
        "\n",
        "st.title('Consumo y producción de CO2')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "git push"
      ],
      "metadata": {
        "id": "aqe0TOBT-DRj"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}