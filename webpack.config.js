const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  mode: 'none',
  context: __dirname,
  entry: [
    './pipeline/static/js/pipeline.js',
    './pipeline/static/css/pipeline.scss',
  ],
  output: {
    path: path.resolve('./pipeline/static/webpack_bundles/'),
    filename: '[name]-[hash].js'
  },

  plugins: [
    new BundleTracker({ filename: './webpack-stats.json' }),
    new MiniCssExtractPlugin({
      filename: '[name]-[hash].css',
      chunkFilename: '[id].css'
    })
  ],
  module: {
    rules: [
      {
        test: /\.(png|jpg|gif)$/,
        use: [
          {
            loader: 'file-loader',
            options: {}
          }
        ]
      },
      {
        test: /\.(scss)$/,
        use: [
          'style-loader',
          {
            loader: MiniCssExtractPlugin.loader,
            options: {}
          },
          {
            loader: 'css-loader',
            options: {
              importLoaders: 1
            }
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  'postcss-import',
                  'precss',
                  'autoprefixer',
                  'postcss-preset-env',
                  'cssnano'
                ]
              }
            }
          },
          'sass-loader'
        ]
      },
      {
        test: /\.(js|ts)$/,
        exclude: /node_modules/,
        use: [{
          loader: "babel-loader",
          options: {
            "presets": [
              "@babel/preset-env",
              "@babel/preset-typescript"
            ],
            "plugins": [
              "@babel/proposal-class-properties"
            ]
          }
        }],
      }
    ]
  }
}
