const passport = require('passport')
const HeaderAPIKeyStrategy = require('passport-headerapikey').HeaderAPIKeyStrategy
const User = require('../models').User

passport.use(new HeaderAPIKeyStrategy(
    { header: 'X-API-Token', prefix: ''},
    false,
    function(apiKey, done) {
        User.findOne({ apiKey: apiKey})
            .then(user => {
                if (!user) { return done(null, false); }
                return done(null, user)
            })
            .catch(err => {
                return done(err, null)
            });
    }
));

module.exports = function (req, res, next) {
    passport.authenticate('headerapikey', { session: false })(req, res, next);
}