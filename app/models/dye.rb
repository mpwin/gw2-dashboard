class Dye < ApplicationRecord
  validates_presence_of :api_id

  serialize :base_rgb, Array
end
