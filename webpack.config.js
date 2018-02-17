const path = require('path')

const devContentBase = path.resolve('./docs-dev/')
module.exports = {
    entry: [
        'babel-polyfill',
        './src/index.js'
    ],
    output: {
        filename: 'bundle-dev.js',
        path: devContentBase
    },

    devServer: {
        contentBase: devContentBase,
        compress: true,
        port: 9000
    },

    // Enable sourcemaps for debugging webpack's output.
    devtool: 'cheap-module-eval-source-map',

    resolve: {
        extensions: ['.js', '.json'],
        modules: [
            path.resolve('./src'),
            'node_modules'
        ]
    },

    module: {
        rules: [{
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader'
        }, {
            test: /\.css$/,
            loader: "style-loader!css-loader?importLoaders=1"
        }, {
            test: /\.(png|woff|woff2|eot|ttf|svg)$/,
            loader: 'url-loader?limit=100000'
        }]
    },

    node: {
        fs: "empty"
    }
}