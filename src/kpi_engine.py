{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e95a53eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "def get_connection():\n",
    "    # Usa la ruta completa que compartiste\n",
    "    return sqlite3.connect(r'C:\\Users\\Jesus Sanchez\\Desktop\\ALEXIS\\1. Pre-Trabajo\\1. Supply Chain Intelligence\\data\\processed\\retail_vault.db')\n",
    "\n",
    "def get_monthly_revenue():\n",
    "    conn = get_connection()\n",
    "    query = \"\"\"\n",
    "    SELECT strftime('%Y-%m', InvoiceDate) AS Month, \n",
    "           SUM(Quantity * Price) AS Revenue\n",
    "    FROM transactions\n",
    "    GROUP BY Month\n",
    "    ORDER BY Month;\n",
    "    \"\"\"\n",
    "    df = pd.read_sql(query, conn)\n",
    "    conn.close()\n",
    "    return df\n",
    "\n",
    "def get_top_countries(n=5):\n",
    "    conn = get_connection()\n",
    "    query = f\"\"\"\n",
    "    SELECT Country, SUM(Quantity * Price) AS TotalSales\n",
    "    FROM transactions\n",
    "    GROUP BY Country\n",
    "    ORDER BY TotalSales DESC\n",
    "    LIMIT {n};\n",
    "    \"\"\"\n",
    "    df = pd.read_sql(query, conn)\n",
    "    conn.close()\n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
