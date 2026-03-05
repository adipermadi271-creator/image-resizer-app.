name: Build APK
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4

      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'

      - name: Install Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y git zip unzip autoconf libtool pkg-config zlib1g-dev \
          libncurses5-dev libncursesw5-dev libtinfo6 cmake libffi-dev libssl-dev \
          python3-pip python3-setuptools

      - name: Install Buildozer & Cython
        run: |
          # Perintah instalasi tanpa --break-system-packages untuk Ubuntu 22.04
          pip3 install --user --upgrade buildozer cython==0.29.33

      - name: Build with Buildozer
        run: |
          export PATH=$PATH:$HOME/.local/bin
          # Menjalankan build secara otomatis
          buildozer android debug
        env:
          ACCEPT_SDK_LICENSE: "yes"

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Aplikasi-Resize-Sukses
          path: bin/*.apk
